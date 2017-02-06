import csv
from haversine import haversine

#list of all houses within radius
def get_neighbors(lat, lon):
    
        house = (lat, lon)
        neighbors = []

        with open('elevations.csv', 'rU') as f:
                reader = csv.reader(f)
                for row in reader:
                    
                        #don't include original in nieghbors
                        if (row[0] == str(lat)) and (row[1] == str(lon)):
                                continue
                        n = (float(row[0]), float(row[1]))
                        distance = haversine(house, n, miles=True)
                        if distance <=0.05 and (n not in neighbors):
                            #append lat, long, elev of nearby neighbor
                            neighbors.append((float(row[0]), float(row[1]), float(row[2])))
        return neighbors

#read elevation from csv given lat, long      
def get_elevation(house):

	# house is a (lat,long) tuple
	lat = house[0]
	lon = house[1]
	elevation = 0

	with open('elevations.csv', 'rU') as f:
		reader = csv.reader(f)

		for row in reader:
			if (row[0] == str(lat)) and (row[1] == str(lon)):
				elevation = float(row[2])

	return elevation

#return percent of non-obstructed
def calc_view(location, neighbors):
        obstructing = 0
        mainElev = get_elevation(location)
        
        #neighbors is list of all neighbors in format (lat, long, elevation)
        if neighbors:
                for n in neighbors:
                    #if elevation of neighbor is higher than main elevation, inc obstructing count
                        if n[2] > mainElev:
                                obstructing += 1
                                print ("%s, %s -- elevation: %d. BLOCKS VIEW." %(n[0], n[1], n[2]))
                        else:
                                print ("%s, %s -- elevation: %d. DOES NOT BLOCK VIEW." %(n[0], n[1], n[2]))
        
        #return ratio of obstructing over total
        return (float(obstructing)/float(len(neighbors)))*100


#return latitude and longitude from csv given APN
def get_location(apn):

        house_lat = 0
        house_lon = 0

        with open('elevations.csv', 'rU') as f:
                reader = csv.reader(f)
                for row in reader:
                    #5th col has APN
                    if row[4] == apn:
                        house_lat = float(row[0])
                        house_lon = float(row[1])

        return (house_lat, house_lon)


if __name__ == '__main__':
    APN = raw_input("Enter the APN of a property whose view\nyou wish to evaluate: ")
    lat, lon = get_location(APN)
    neighbors = get_neighbors(lat, lon)
    if neighbors:
        print
        print("Number of neighbors: " + str(len(neighbors)) + "\n")
        print ("Elevation of selected property: %s" % get_elevation((lat,lon)) + "\n")
        print ("Neighboring properties: ")
        print ("\nPercentage of view not blocked by\nneighboring properties: %d%%" %((calc_view((lat, lon), neighbors))))
    else:
        print("The APN "+ APN + " has no known neighbors.")
        
    

