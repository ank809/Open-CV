import numpy as np
x= [1, 2, 3,4, 5, 6]
print(x)
print(type(x))

arr1= np.array(x)
print(type(arr1))

print(np.arange(1, 13))

# suppose if you want to print in gap of 2
print(np.arange(1, 14, 2))

# important for image generation
print(np.zeros((2, 4)))
print(np.ones((3, 4)))

#  if you want to print random variables in a range
#  suppose you do not want to change the order then
#  here we give 23 as if want to copy the array and want to have the same order as above one
np.random.seed(23)
print(np.random.randint(2, 99, 50))

arr2= np.random.randint(2, 99, 50)
print(arr2)

arr3= arr2.reshape(10, 5)
print(arr3)

print(arr3.max())
print(arr3.min())
print(arr3.mean())
print(arr3.argmax())
print(arr3.argmin())

print(arr3.shape)

row=3
col=4
print(arr3[row, col])

#  this will print only column
print(arr3[:,4])

#  this will print only rows
print(arr3[2,:])

# for printing a range in this range is exclusive
print(arr3[0:2, 0:3])

#  assigning a particular range of elements to a new  element
arr3[0:4, 0:3]=1
print(arr3)

#  copying into a new array
arr4= arr3.copy()
print(arr4)