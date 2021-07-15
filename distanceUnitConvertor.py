#program for distance conversion

dist_in_km=int(input("Enter distance in kms: "))
print(dist_in_km," kms")
#to miles
dist_in_miles=dist_in_km/1.609
print(dist_in_miles," miles")
#to meters
dist_in_m=dist_in_km*1000
print(dist_in_m," meters")

#to centimeter
dist_in_cm=dist_in_km*100000
print(dist_in_cm," centimeters")

#to millimeters
dist_in_mm=dist_in_m*1000
print(dist_in_mm," millimeters")

#to micrometers
dist_in_mcm=dist_in_mm*1000
print(dist_in_mcm," micrometers")

#to nanometers
dist_in_nm=dist_in_mcm*1000
print(dist_in_nm," nanometers")

#to yards
dist_in_yards=dist_in_km*1094
print(dist_in_yards," yards")

#to foot
dist_in_foot=dist_in_km*3281
print(dist_in_foot," foot")

#to inch
dist_in_inch=dist_in_km*39370
print(dist_in_inch," inches")

#to nautical mile
dist_in_naut_mile=dist_in_km/1.852
print(dist_in_naut_mile," nautical miles")