# This project will examine Blue Whales and Killer Whales sightings in
# Nova Scotia and assess their roaming area.
# The csv file is turned into a shapefile and the correct species are filtered out
# The File takes all Killer Whale and all Blue Whale sightings and buffers a 50 mile zone around each point
# These buffers are then intersected
# The roaming area in square miles is also calculated and can be found in the attricube table of the Intersect file.
# The polygon of whale sightings/roaming area is then modified to exclude overland areas around Nova Scotia.
# This erase polygon ONLY exludes Nova Scotia land area as using other polygons along the Canadian coastline yielding large and unnecessary file sizes. 
