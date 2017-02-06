import googlemaps
import csv

gmaps = googlemaps.Client(key='insert key here')

core = open("corelogic.csv", "rU")

fileRead = csv.reader(core)
lines = list(fileRead)

out = open("output.txt", 'a+')

#lat and long are indeces 0 and 1
for i in lines:
    if i[0] != "NULL":
        geocode_result = gmaps.elevation((float(i[0]), float(i[1])))
        out.writelines(str(i[0]) + ", " + str(i[1]) + ", " + str(geocode_result[0].get('elevation')) + "\n")
    else:
        #return none if no lat/long in row
        out.writelines("None" + "\n")

core.close()
out.close()
