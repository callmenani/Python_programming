my_travel = [
{
  "Country" : "Newzealand",
  "Visted" : 6,
  "Places_Visited" : ["Tauranga" , "Christ_church" , "Auckland"]
},
{
  "Country" : "US",
  "Visted" : 3,
  "Places_Visited" : ["New York" , "San Fransisco" , "Texas"]
},
]
def add_country(country , visited , places):
    new_dict = {}
    new_dict["Country"] = country
    new_dict["Visited"] = visited
    new_dict["Places_Visited"] = places
    my_travel.append(new_dict)

add_country("Uk",3,["Switzerland","London","Manchester"])
print(my_travel)