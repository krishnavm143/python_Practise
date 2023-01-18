my_Dict={
    "name":"krishna",
    "age":27,
    "city":"bidar",
    "state":"karnataka"
}
print(my_Dict.keys())
print(my_Dict.values())
print(my_Dict.items())

new_dict_add={
    "education":"Btech",
    "college":"Mvj College Of Engineering"
}
my_Dict.update(new_dict_add)
print(my_Dict)
print(my_Dict.get('city'))