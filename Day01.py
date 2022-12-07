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
odd = [1,3,5,7]
arr = arr+odd #odd list will be appended after list arr
print(arr)
print(["Hi"]*3)

#Insert in list
odd.insert(1,30)
# print(odd) #30 will be inserted in index 1
odd[2:3] = [5,8]
print(odd)

#delete in list
del odd[2]
print(odd) #index present at element 2 will deleted
del odd[2:3]
print(odd)

#clear a list
odd.clear()
print(odd)
odd = ['p','r','o','b','l','e','m']
x  = odd.pop(1) #item will be removed from index 1
print(x)
print(odd)

odd.remove('p') #removed wrt elements
print(odd)

#List comprehension : use to create a list from an existing list
pow2 = [x**2 for x in range(10+1)]
print(pow2)
odd = [x for x in range(20) if x % 2 == 1]
print(odd)

#Find an element in list
print(3 in odd) #True
print(odd.index(3)) #Return the index of that element
index = odd.index(7, 3, 5)   # (search item, start index, end index)
print('The index of i:', index) 

#Count 
#syntax : list.count(element)
vowels = ['a', 'e', 'i', 'o', 'i', 'u']
cnt = vowels.count('i')
print("i in vowels: ", cnt)

random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]
count = random.count([3, 4])
print(count)

#List sort()
#syntax: list.sort()
prime_numbers = [11, 3, 7, 5, 2]

prime_numbers.sort()
print(prime_numbers) #By default ascending order
prime_numbers.sort(reverse=True)
print(prime_numbers) #Descending order

#Reverse the list
prime_numbers.reverse()
print(prime_numbers)

#Copy list
li = prime_numbers
print(li)
print(prime_numbers)
li = prime_numbers.copy()
print(li)