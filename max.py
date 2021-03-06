# Valerie Walsh 22-04-2018
# Iris Data Set project
# Reference: Topic 7 videos
# Max of each column

import numpy
data = numpy.genfromtxt('iris.csv', delimiter=',')

maxfirstcol = numpy.max(data[:,0])
maxsecondcol = numpy.max(data[:,1])
maxthirdcol = numpy.max(data[:,2])
maxforthcol = numpy.max(data[:,3])

print('\n')

print("First column max is:", maxfirstcol)

print("Second column max is:", maxsecondcol)

print("Third column max is:", maxthirdcol)

print("Forth column max is:", maxforthcol)

print('\n')

# Reference: https://www.tutorialspoint.com/python/list_min.htm
# An alternative and cleaner solution which I found to the above is;

print("The max of each column is:", maxfirstcol, maxsecondcol, maxthirdcol, maxforthcol)

print('\n')
