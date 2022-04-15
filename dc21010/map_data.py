import sys
import pandas as pd
import plotly.express as px

if len(sys.argv) != 2:
    print("Usage: python {} <input_file_name.csv>".format(sys.argv[0]))
    sys.exit()

input_file_name = sys.argv[1]

data = pd.read_csv(input_file_name)

# fig = px.scatter_mapbox(data, lat="lat", lon="long", color="year+type", zoom=13)
fig = px.scatter_mapbox(data, lat="START LAT", lon="START LONG", color="MINUTES", zoom=13)

fig.update_layout(mapbox_style="open-street-map", mapbox_center_lat = 38.99,
    margin={"r":0,"t":0,"l":0,"b":0})

fig.show()