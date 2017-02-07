import gmplot
import csv
from haversine import haversine
from find_neighbors import get_location, get_neighbors, get_elevation

def calc_blocking_n(location, neighbors):

	b_neighbors = []
	if neighbors:

		for n in neighbors:

			if get_elevation(n) > get_elevation(location):
				b_neighbors.append(n)

	return b_neighbors

if __name__ == "__main__":
	lat, lon = get_location('insert APN here')
	neighbors = get_neighbors(lat, lon)

	blocking_neighbors = calc_blocking_n((lat,lon), neighbors)
	unblocking_neighbors = [n for n in neighbors if not n in blocking_neighbors]

	u_neighbor_lats = [i[0] for i in unblocking_neighbors]
	u_neighbor_lons = [i[1] for i in unblocking_neighbors]


	b_neighbor_lats = [i[0] for i in blocking_neighbors]
	b_neighbor_lons = [i[1] for i in blocking_neighbors]


	gmap = gmplot.GoogleMapPlotter(lat, lon, 16)
	
	#Plot original home
	gmap.marker(lat, lon, 'r')
	
	#Plot neighbors who do not obstruct view in gray
	gmap.scatter(u_neighbor_lats, u_neighbor_lons, 'lightslategray', marker=True)
	#plot neighbors who do obstruct view in black
	gmap.scatter(b_neighbor_lats, b_neighbor_lons, 'k', marker=True)

	#create html file with map
	gmap.draw("view.html")




