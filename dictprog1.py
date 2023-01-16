#declare dictionary
#extract values from the given dictionary

test_dict = { 'the' : [23,44,56,7,7],
              'beast' :[32,5,2,34,5],
              'incarnate' :[2,4,5,6,7],
              'brock lesnar' : [1,4,7]}

#printing original dictionary
print("the OG  dictionary is: "+ str(test_dict))

#extract unique values dictionary values
x = []

#for loop for keys
for i in test_dict.keys():

#extend() function
    x.extend(test_dict[i])
x = list(set(x))
x.sort()

#printing result
print("the unique value list is: " +str(x))