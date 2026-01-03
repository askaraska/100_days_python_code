#==============================SESSION 2: NESTING LIST AND DICTIONARIES===================================#
#1.NESTED LIST IN DICTIONARY:

travel_log = {
    "France" : ["paris","Lille","dijon"],
    "Germany" : ["stuttgart","berlin"],
}

print(travel_log) #{'France': ['paris', 'Lille', 'dijon'], 'Germany': ['stuttgart', 'berlin']}

#Print lille:
print(travel_log["France"]) #['paris', 'Lille', 'dijon']
print(travel_log["France"][1]) #Lille

#2.NESTED LIST: in list
nested_list =["a","b",["c","d"]]
print(nested_list)  #['a', 'b', ['c', 'd']]

#how can you retrieve d from list:
print(nested_list[2][1]) # d

#3. NESTING a DICTIONARY INSIDE A DICTIONARY:
travel_logs = {
    "France" : {
        "cities_visited" : ["paris","Lille","dijon"],
        "total_visits" : 5,
    },
    "Germany" : {
        "cities_visited" : ["berlin","hamburg","stuttgart"],
        "total_visits" : 12,
    },
}
print(travel_logs) # gives entire o/p.
#how to access stuttgart:
print(travel_logs["Germany"]) #o/p: {'cities_visited': ['berlin', 'hamburg', 'stuttgart'], 'total_visits': 12}
print(travel_logs["Germany"]["cities_visited"]) #o/p: ['berlin', 'hamburg', 'stuttgart']
print(travel_logs["Germany"]["cities_visited"][2]) #o/p: stuttgart