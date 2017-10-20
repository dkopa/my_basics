# List Comprehension - returns multiple variables 
fName, fLabels = zip(*[(x.split()[0], int(x.split()[1])) for x in tList])
