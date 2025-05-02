# GEE-Data-Extraction <br />

Created ETL data pipeline to extract satellite imagery data for a **Pakistan** over the past year (2024) using Google Earth Engine (GEE), and process the data to calculate **NDVI (Normalized Difference Vegetation Index is a metric used to measure the health and density of vegetation)** and store the processed data in a PostgreSQL database for further analysis. Visualize the data in a Webapp using NDVI color scheme.<br /><br /><br />

![ETL Diagram](https://github.com/zaid638/GEE-Data-Extraction/blob/main/GEE%20ETL%20Diagram%203.png) <br /><br /><br />

## Tools and Technologies Used <br />

1. **Google Earth Engine:** Accessing and processing satellite imagery data.
2. **Python:** Create pipeline for Extract, Transform and Load the data.
3. **PostgreSQL:** Store the processed data.
4. **Streamlit:** Create webapp for visualize data.<br /><br /><br />


## Steps Involved <br /><br />

### Step 1: Setup and Initialization <br />

1. Authenticate and initialize the Google Earth Engine API in Python.
2. Define the Area of Interest (AOI) using geographical coordinates (Pakistan, splitted into provinces).
3. Specify the time range for data extraction (past one year, splitted into months).<br /><br />


### Step 2: Data Extraction from GEE <br />

1. Extract Coordinates:
   - Extracted the coordinates of each province.
2. Dataset Selection:
   - Used Sentinel-2 surface reflectance data.
3. Filtering Criteria:
   - Date range: January 1, 2024, to December 31, 2024.
   - Spatial range: AOI defined for the specific region (Pakistan).
4. Extract NDVI data:
   - Extracted data for each province (ID, Date, Latitude, Longitude, NDVI).<br /><br />

### Step 3: Data Transformation <br />

1. Removed the rows that containing NULL values in NDVI column.
2. Extracted date value manually from ID column.
3. Reduced the spatial resolution based on needs (100/1000/1500 meters).
4. Divided the time range into monthly chunks to limit the number of images queried at a time.
5. Filtered images by cloud cover to reduce unnecessary data.
6. Covert data points into Dataframe.<br /><br />

### Step 4: Load the Data <br />

1. Created a Database for every province in PostgreSQL.
2. Created table for every month in each database.
3. Inserted data into a PostgreSQL database.<br /><br />

### Step 5: Data Visualization <br />

1. Addressed issues such as missing dates in images.
2. Split queries into manageable chunks to avoid exceeding GEE's element limits.<br /><br /><br />

## Results <br /><br />

1.	NDVI values and Dates were successfully extracted for all Provinces of Pakistan in 2024.
2.	The data were stored in a PostgreSQL database for further analysis.
3.	Created Webapp to visualized the NDVI data points.<br /><br /><br />

