# GEE-Data-Extraction <br />

Created ETL data pipeline to extract satellite imagery data for **Pakistan** over the past year  using Google Earth Engine (GEE), and process the data to calculate **NDVI (Normalized Difference Vegetation Index is a metric used to measure the health and density of vegetation)** and store the processed data in a PostgreSQL database for further analysis. Visualize the data in a web app using the NDVI color scheme.<br /><br /><br />

![ETL Diagram](https://github.com/zaid638/GEE-Data-Extraction/blob/main/GEE%20ETL%20Diagram%205.png) <br /><br /><br />

---

## Tools and Technologies Used <br />

1. **Google Earth Engine:** Accessing and processing satellite imagery data.
2. **Python:** Create pipeline for Extract, Transform, and Load the data.
3. **PostgreSQL:** Store the processed data.
4. **Streamlit:** Create a web app to visualize data.<br /><br /><br />


## Steps Involved <br /><br />

### Step 1: Setup and Initialization <br />

1. Authenticate and initialize the Google Earth Engine API in Python.
2. Define the Area of Interest (AOI) using geographical coordinates (Pakistan, split into provinces).
3. Specify the time range for data extraction (past one year, split into months).<br /><br />


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

1. Removed the rows that contained NULL values in the NDVI column.
2. Extracted date value manually from ID column.
3. Reduced the spatial resolution based on needs (100/1000/1500 meters).
4. Divided the time range into monthly chunks to limit the number of images queried at a time.
5. Filtered images by cloud cover to reduce unnecessary data.
6. Covert data points into a Dataframe.<br /><br />

### Step 4: Load the Data <br />

1. Created a Database for every province in PostgreSQL.
2. Created a table for every month in each database.
3. Inserted data into a PostgreSQL database.<br /><br />

### Step 5: Data Visualization <br />

1. Created a Webapp Using Streamlit. 
2. Visualize the data using filters.<br /><br /><br />

![App Diagram](https://github.com/zaid638/GEE-Data-Extraction/blob/main/collage1.png) <br /><br />

![Map Diagram](https://github.com/zaid638/GEE-Data-Extraction/blob/main/collage2.png) <br /><br /><br />

## Results <br /><br />

1.	NDVI values and Dates were successfully extracted for all Provinces of Pakistan in 2024.
2.	The data were stored in a PostgreSQL database for further analysis.
3.	Created a Webapp to visualize the NDVI data points.<br /><br /><br />

## Challenges and Solutions<br /><br />

### Challenge 1: GEE Query Limitations<br />

- Reason: Large AOI, fine resolution, and a large number of images can’t be extracted at once. 
- Solution:
   * Extracted the coordinates of each province rather than the entire country.
   * Reduced resolution based on coordinates.
   * Collected the monthly data.
   * Filtered by cloud cover.<br /><br />
   
### Challenge 2: Missing Dates Property<br />

- Reason: Some Images lacked timestamp metadata. 
- Solution:
   * Applied manual date extraction method.<br /><br />
   
## Future Work<br /><br />

1. Automate the Pipeline using Apache Airflow and Collect data for every month. 
2. Implement machine learning models for predictive analysis.<br /><br />
