import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import layers, models, optimizers
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date
import rasterio

# Function to load Sentinel-2 data
def load_sentinel_data(api, area, start_date, end_date):
    footprint = geojson_to_wkt(area)
    products = api.query(footprint,
                         date=(start_date, end_date),
                         platformname='Sentinel-2',
                         cloudcoverpercentage=(0, 30))

    # Download the first product
    for product_id in products:
        api.download(product_id)
        # You can return the product ID or the file paths for further processing
        # return product_id
        break  # Download only the first product for demonstration purposes

# Function to process Sentinel-2 data and extract images
def process_sentinel_data(file_path):
    # Example code for processing Sentinel-2 data and extracting images
    # Replace this with your actual data processing code
    with rasterio.open(file_path) as src:
        data = src.read()  # Read the data from the raster file
        # Process data as needed
    return data

# Modified load_data function
def load_data(api, area, start_date, end_date):
    # Load Sentinel-2 data
    file_path = load_sentinel_data(api, area, start_date, end_date)
    # Process Sentinel-2 data and extract images
    data = process_sentinel_data(file_path)
    return data

# Example usage
def main():
    # Define SentinelAPI
    api = SentinelAPI('your_username', 'your_password', 'https://scihub.copernicus.eu/dhus')

    # Define the area of interest as a GeoJSON polygon
    area_of_interest = {
        "type": "Polygon",
        "coordinates": [[[11.0, 46.5], [11.0, 47.0], [11.5, 47.0], [11.5, 46.5], [11.0, 46.5]]]
    }

    # Load data
    data = load_data(api, area_of_interest, date(2024, 1, 1), date(2024, 1, 31))

    # Example usage of the loaded data
    print("Data shape:", data.shape)

if __name__ == "__main__":
    main()