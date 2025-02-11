phoneboook = {
    "John" : 93838298348293,
    "Jack" : 29303020392030,
    "Jill" : 38472947234829,
}

phoneboook["Jake"] = 3998832939293
del phoneboook["Jill"]

if "Jake" in phoneboook:
    print ("Jake is listed in the phonebook")

if "Jill" not in phoneboook:
    print("Jill is not listed i th phonebook")