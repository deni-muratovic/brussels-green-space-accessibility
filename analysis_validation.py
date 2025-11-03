# Brussels Green Space Access - Analysis Validation
import geopandas as gpd

# Load the results
results = gpd.read_file("final_results.geojson")

# Calculate key statistic
total_population = 1249597
served_population = results['calc_pop'].sum()
access_percentage = (served_population / total_population) * 100

print("Brussels Green Space Access Results:")
print(f"Total population with park access: {served_population:,.0f}")
print(f"Total Brussels population: {total_population:,.0f}")
print(f"Percentage with access: {access_percentage:.1f}%")
