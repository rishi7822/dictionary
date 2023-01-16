#merging dictionary
def Merge(dict1, dict2):
    return(dict2.update(dict1))

#driver code
dict1 = {"cristaino":7,"messi":10}
dict2 = {"dhoni":7,"kohli":10}

#returns none
print(Merge(dict1, dict2))


#changes or updates
print(dict2)