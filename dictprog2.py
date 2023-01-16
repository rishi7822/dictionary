#program to print the sum in dictionary
def returnSum(dict):

    sum  = 0
    for i in dict:
        sum = sum + dict[i]
    
    return sum

#driver function
dict = {'a':199, 'b':2002, 'c':999}
print("Sum :", returnSum(dict))