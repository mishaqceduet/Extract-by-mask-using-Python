# Extract-by-mask-using-Python
Extracting Area of Interest from a global DEM raster using Python

## Requirements

- Python 3.6 or higher
- geopandas
- rasterio
- pandas
- numpy

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/Extracting_Chitral_DEM.git
    cd Extracting_Chitral_DEM
    ```

2. **Install the required libraries:**

    ```sh
    pip install geopandas rasterio pandas numpy
    ```

3. **Ensure your directory structure matches the following:**

    ```
    .
    ├── Boundary_Shapefile
    │   └── Chitral_Boundary.shp
    ├── Output DEM_Chitral
    │   └── (this will contain the output file after running the script)
    ├── Extracting_Chitral.py
    └── README.md
    ```

## Usage

1. **Run the script:**

    Ensure you are in the project directory and run:

    ```sh
    python Extracting_Chitral.py
    ```

2. **Check the output:**

    After running the script, the masked DEM for the Chitral study area will be saved in the `Output DEM_Chitral` directory as `Chitral_DEM_Masked.tif`.

## Script Overview

The script performs the following steps:

1. **Import necessary libraries:**
    - Imports `geopandas`, `rasterio`, `rasterio.mask`, `numpy`, `pandas`, and `os`.

2. **Set file paths:**
    - Defines paths for the shapefile and DEM.

3. **Load the shapefile and DEM:**
    - Reads the shapefile using `geopandas` and the DEM using `rasterio`.

4. **Reproject shapefile if necessary:**
    - Checks if the shapefile CRS matches the DEM CRS and reprojects if necessary.

5. **Extract the geometry from the shapefile:**
    - Extracts the geometry coordinates from the shapefile.

6. **Clip the DEM using the shapefile geometries:**
    - Uses `rasterio.mask.mask` to clip the DEM with the shapefile geometries.

7. **Update metadata and save the clipped DEM:**
    - Updates the metadata for the clipped DEM and saves it to the specified output path.

8. **Convert clipped DEM to a DataFrame:**
    - Converts the clipped DEM to a numpy array and then to a Pandas DataFrame for further analysis.

9. **Print the first few rows of the DataFrame:**
    - Prints the first few rows of the DataFrame to the console.

## Notes

- Ensure the shapefile and DEM paths are correctly specified.
- The script assumes that the input files are in the correct format and CRS.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

Special thanks to [your name] for providing guidance and support during the development of this project.
