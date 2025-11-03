# brussels-green-space-accessibility
A spatial equity analysis of public park accessibility in Brussels. This project uses network analysis and data curation to reveal that only 17.5% of residents have walking access to public parks ≥1 hectare.

# Green Space Access in Brussels

## The Problem
Public green space distribution in Brussels is known to be unsatisfactory and unequal. However, the official GIS data from UrbIS displays many more polygons representing green spaces than is expected. This can distort perceptions of equitable accessto green spaces.

## The Investigation
I discovered the data included every green patch (highway medians, private lawns, cemeteries etc.) as "green spaces". This, however, doesn't tell us how accessible these green spaces are to the public.

## The Solution  
1. **Data Curation:** Used the official data from garden.brussels along with OpenStreetMaps and Google Maps to digitize the 126 public green spaces in Brussels. Then I used my curated layer to extract the corresponding, high-precision geometries from the official UrbIS layer. I only used green spaces of 1ha or more.

2. **Network Analysis**: Used OSM to extract the road network of Brussels, focused on footpaths, bicycle lanes and paths for horseriding. Used the intersections of these paths with the filtered out green space geometries to determine and place access points. Then I created a service area layer, buffered it by 10 meters and intersected it with the official municipalities layer of Brussels that contains population numbers. The focus was on pedestrian access to green spaces within 400 meters. This provided a realistic model of pedestrian access, moving beyond simplistic straight-line buffers.

3. **Validation:** Prior to doing the network analysis, I performed an Euclidean distance analysis on the UrbIS layer in its original form, and the percentage was much higher than expected at 78.8%. The Euclidean distance approach, paired with the unfiltered indiscriminate official UrbIS green space layer can create a misleading image of green space access in Brussels.

## The Finding
Only **17.5%** of residents have practical park access, revealing significant urban inequality. This result starkly contrasts with the 78.8% access suggested by a naive analysis of the raw data, demonstrating the critical importance of methodological rigor in urban equity analysis.

## Technical Implementation
```python
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

```sql
-- Conceptual spatial SQL for the same analysis
-- Calculate green space access
SELECT 
    SUM((POPULATION_NUMERIC * ST_Area(geom)) / AREA) AS total_served_population,
    (SUM((POPULATION_NUMERIC * ST_Area(geom)) / AREA) / 1249597) * 100 AS access_percentage
FROM 
    intersection_final;
