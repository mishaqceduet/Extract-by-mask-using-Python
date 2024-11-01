import geopandas as gpd
import rasterio
from rasterio.mask import mask
import numpy as np
import pandas as pd
import os

#Paths to be used for the input files
shapefile_path = r'D:\Python_Practice\Extracting_Chitral\Boundary_Shapefile\Chitral_Boundary.shp'
dem_path = r'D:\Python_Practice\Extracting_Chitral\diva_Pak_WGS_1984.tif'
output_path = r'D:\Python_Practice\Extracting_Chitral\Output DEM_Chitral\Chitral_DEM_Masked.tif'  # Path to save the masked DEM

# Loading the shapefile of Chitral which is my study Area
shapefile = gpd.read_file(shapefile_path)

# Load the DEM Tile , the bigger tile with Chitral inside
dem = rasterio.open(dem_path)

# Reproject shapefile to the same CRS as the DEM if necessary
if shapefile.crs != dem.crs:
    shapefile = shapefile.to_crs(dem.crs)

# Get the geometry coordinates from the shapefile
geometries = [feature["geometry"] for feature in shapefile.__geo_interface__["features"]]

# Clip the DEM using the shapefile geometries
DEM_Chitral, out_transform = mask(dem, geometries, crop=True)

# Update the metadata for the clipped DEM
out_meta = dem.meta.copy()
out_meta.update({
    "driver": "GTiff",
    "height": DEM_Chitral.shape[1],
    "width": DEM_Chitral.shape[2],
    "transform": out_transform
})

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Save the clipped DEM to a new file
with rasterio.open(output_path, "w", **out_meta) as dest:
    dest.write(DEM_Chitral)

# Cthe next step is to convert the clipped DEM to a numpy array
dem_array = DEM_Chitral[0]

# Getting the Pixel coodinates for DEM
row_indices, col_indices = np.indices(dem_array.shape)

# Changing the  pixel coordinates to geographic coordinates
x_coords, y_coords = rasterio.transform.xy(out_transform, row_indices, col_indices)

# Flatten the arrays is an important step for coordinates
dem_values = dem_array.flatten()
x_coords_flat = np.array(x_coords).flatten()
y_coords_flat = np.array(y_coords).flatten()

# Now Creating the  Pandas DataFrame for my work
dem_dataframe = pd.DataFrame({
    'X': x_coords_flat,
    'Y': y_coords_flat,
    'Elevation': dem_values
})

# Drop no-data values if any
dem_dataframe = dem_dataframe[dem_dataframe['Elevation'] != dem.nodata]

# Reset the index
dem_dataframe.reset_index(drop=True, inplace=True)

print(dem_dataframe.head())


