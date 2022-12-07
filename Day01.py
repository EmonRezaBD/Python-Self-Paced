# print('Bimillah')
#split function
txt = "Welcome to python"
x = txt.split()
print(x[0])

#lists
my_list = [1,2,3,4]
print(my_list[2]) #3
print(my_list[-1],len(my_list)) #4

#Nested list
nestedList = ["Happy", [2,1,5,0,-10]]
print(nestedList[0])
print(nestedList[1][-1])

#list slicing
my_list = ['p','r','o','g','r','a','m','i','z']
print(my_list[2:5])
print(my_list[5:]) # [start : end]
print(my_list[:5]) #start index is inclusive but end index is exclusive

#update elements in list
arr = [2,3,34,4,5]
arr[0]=20
print(arr) #first ele got 20
arr[1:3] = [40,50]
print(arr)

#Push_back or append an ele
arr.append(90)
#to add more than one elements use extend
arr.extend([100,110,120])
print(arr)

#list concatenation
