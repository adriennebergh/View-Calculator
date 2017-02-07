# View-Calculator
@author Adrienne Bergh
@author Nicholas Vega
@author Kayla Ziegler

Entry for the 2017 CoreLogic Grand Challenge

CoreLogic provided participants of the Challenge with property data for approx. 65,000 homes in the San Diego area.
Our program consists of 3 main parts:
- Elevation calculator
- Neighboring Algorithm
- Map Plotter

Elevation calculator:
- Reads through the property data and gets the elevation of each home from the Google Maps API

Neighboring Algorithm:
- Determines neighboring properties of a given home using latitude and longitude data from the provided dataset
- Calculates the percentage of that home's view that is obstructed by its neighbors by comparing the homes' elevation data

Map Plotter:
- Plots a given home to a map using the Google Maps API
- Marks each neighbor of the home with either gray if the neighbor is not estimated to block the home's view or black if it is.

All data used in this project is proprietary to CoreLogic.
