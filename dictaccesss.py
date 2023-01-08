#accessing items
#You can access the items of a dictionary by referring to its key name, inside square brackets

data = {
    "id":2022,
    "name":"Batman",
    "class":"DC",
    "movie":"The Dark Knight"
}

x = data["movie"]
print(x)

#get() method
y = data.get("class")
print(y)

#to call the keys
z  = data.keys()
print(z)

#Add a new item to the original dictionary, and see that the keys list gets updated as well:
z = data.keys()

print(z)


data["type"] = "vigilant"

print(z)


#get values
x = data.values()
print(x)

#
x = data.values()

print(x) #before the change

data["year"] = 2007

print(x) #after the change

if "model" in data:
  
 print("No, 'model' is not  one of the keys in the thisdict dictionary")