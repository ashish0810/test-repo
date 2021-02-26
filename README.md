# DC2021 - Team 10

Ashish Bachavala and Matt Braun

## Presentation is in the `presentation` folder

The website is hosted here: [https://ashishbach.com/dc21/](https://ashishbach.com/dc21/)

## Scripts and explanations

### clean_data.py

Takes raw data and filters out the data that we determined to be "bad" data and separates it into two different files.

### add_campus.py

Takes data and boundaries file and adds two columns, indicating if the trip started or ended on campus.

### add_money.py

Takes data and adds a column, calculating the cost of the trip based on the type of vehicle and minutes ridden.

### add_ride_counts.py

Takes data and customer ride counts file and adds a column, indicating how many total rides that customer has been on.

### count_rides.py

Takes data and outputs the list of unique customer ids and the number of rides they have been on.

### process_boundaries.py

Takes the restricted and parking zones file given to us and reshapes it into a form for us to use it easier.

### process_data.py

Takes data and reshapes it into a form for us to use it better.

### point_in_polygon.py

Contains one function which takes a list of points representing a boundary and another single point and returns if that point is within that boundary or not.

### map_boundaries.py

Plots the boundaries, parking zones, and geofence on a map and displays it.

### map_data.py

Plots the specified data on a map and displays it.

### export_map.py

Same as map_data.py but also exports to a html file to be hosted online.
