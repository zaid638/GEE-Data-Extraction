import ee
import psycopg2
from datetime import datetime, timedelta, timezone, date
import pandas as pd



def get_coords():
    countries = ee.FeatureCollection("USDOS/LSIB_SIMPLE/2017")
    roi = countries.filter(ee.Filter.eq("country_na", "Pakistan"))
    geometry = roi.geometry()    
    coords = [c3 for c1 in geometry.coordinates().getInfo() for c2 in c1 for c3 in c2]
    splitted_aoi = [coords[i:i + 100] for i in range(0, len(coords), 100)]
    return splitted_aoi



def generate_date_ranges(start_date):
    ranges = []
    current_date = start_date    
    for i in range(1,13):
        if i < 8:
            if i == 2:
                next_date = current_date + timedelta(days=28)        
            elif i % 2 == 0:
                next_date = current_date + timedelta(days=29)
            else:
                next_date = current_date + timedelta(days=30)
        else:
            if i == 12:
                next_date = current_date + timedelta(days=15)
            elif i % 2 == 0:
                next_date = current_date + timedelta(days=30)
            else:
                next_date = current_date + timedelta(days=29)            
        ranges.append((current_date, next_date))
        current_date = next_date + timedelta(days=1)
    return ranges



def get__monthly_data(month, coords):
    aoi = ee.Geometry.Polygon(coords)

    collection = ee.ImageCollection("COPERNICUS/S2_HARMONIZED") \
        .filterBounds(aoi) \
        .filterDate(month[0].strftime("%Y-%m-%d"), month[1].strftime("%Y-%m-%d")) \
        .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 20)) \
        .map(lambda image: image.normalizedDifference(['B8', 'B4']).rename("NDVI"))

    points = collection.getRegion(aoi, scale=1000).getInfo()
    return points



def get_date(data):
    data_part = data.str.split("_", n=1, expand=True)
    return data_part[0].apply(lambda x: pd.to_datetime(datetime.fromisoformat(x).astimezone(timezone.utc).strftime('%Y-%m-%d')))



def data_transform(points):
    skip_header = points[1:]
    df = pd.DataFrame(skip_header, columns=points[0])
    df.rename(columns={'id': 'ID', 'longitude':'Longitude', 'latitude':'Latitude', 'time':'Date'}, inplace=True)
    df['Date'] = get_date(df['ID'])
    non_missing_NDVI = df[pd.notnull(df["NDVI"])]
    return non_missing_NDVI




def merge_data(coord_list):
    dataframes = []
    month = generate_date_ranges(date(2024, 1, 1))[0]
    try:
        for i,coord in enumerate(coord_list):
            points = get__monthly_data(month, coord)
            dataframe = data_transform(points)
            dataframes.append(dataframe)
        final_dataframe = pd.concat(dataframes, ignore_index=True)
        return final_dataframe
    except:
        print(f"Error in coord {i}")
        final_dataframe = pd.concat(dataframes, ignore_index=True)
        return final_dataframe



def create_table(name):
    cursor = conn.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {name} (
            date DATE,
            latitude FLOAT,
            longitude FLOAT,
            ndvi FLOAT
        );""")
    conn.commit() 




def insert_data_into_database(df):
    cursor = conn.cursor()
    for row in df.itertuples():
        cursor.execute(
        "INSERT INTO Jan_test2 (date, latitude, longitude, ndvi) VALUES (%s, %s, %s, %s)",
        (row.Date, row.Latitude, row.Longitude, row.NDVI))
    conn.commit()
    cursor.close()
    conn.close()





ee.Authenticate()
ee.Initialize(project='ee-zaidahamed638')
print(ee.String('Hello from the Earth Engine servers!').getInfo())



# Connect database

conn = psycopg2.connect(
dbname="test_db",
user="postgres",
password="myfirstDE@rcai",
host="localhost",
port="5432")


# create_table('Jan_test2')

# insert_data_into_database(merge_data(get_coords()))