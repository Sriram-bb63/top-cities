import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

map_df = gpd.read_file("Igismap/Indian_States.shp")

city_csv = gpd.read_file("coordinates.csv")
city_df = gpd.GeoDataFrame(city_csv, geometry=gpd.points_from_xy(city_csv["lat"], city_csv["lon"]))

plt.style.use("seaborn")

base_map = map_df.plot()
city_df.plot(ax=base_map, color="red")

plt.show()