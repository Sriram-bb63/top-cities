import geopandas as gpd
import matplotlib.pyplot as plt

map_df = gpd.read_file("Igismap/Indian_States.shp")

city_csv = gpd.read_file("coordinates.csv")
city_df = gpd.GeoDataFrame(city_csv, geometry=gpd.points_from_xy(city_csv["lon"], city_csv["lat"]))

plt.style.use("seaborn")

base_map = map_df.plot()
city_df.plot(ax=base_map, color="red", marker="v")

plt.title(f"Top {len(city_df)} most populated cities ")

plt.tight_layout()
plt.axis("off")

plt.savefig(f"maps/top_{len(city_df)}.png")

plt.show()