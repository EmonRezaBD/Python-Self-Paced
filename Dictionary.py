test_dict = {'gfg' : {'rate' : 5, 'remark' : 'good'}, 'cs' : {'rate' : 3}}
print(str(test_dict))

for sub in test_dict:
    print(sub)
    for sub_nest in test_dict[sub]:
        print(sub_nest, ":", test_dict[sub][sub_nest])

updict = {"gfg":1, "best":17}

for i in test_dict:
    if i in updict:
        test_dict[i][0]= updict[i]

print(test_dict)

data ={1:'Reza', 2:'Rokon', 3:'Dhrubo Baru'}
# print(data[2])
s = data.get(3, 'Data not found')
print(s)

#COnverting list in dictionary
keys = ['Reza', 'Rokon', 'Dhrubo Baru']
values = ['Python', 'Java', 'JS']
data = dict(zip(keys,values))
print(data)

data['Monica'] = 'baking'
print(data)

del data['Monica']
print(data)

#List and dictionary within a dictionary
prog = {'JS': 'Atom', "CS" :"VS", 'Python': ['pycharm', 'sublime'], 'java': {'JSE':'netbeans', 'JEE':'eclips'}}

print(prog)
print(prog['Python'][0])
print(prog['java']['JEE'])

print(dir(prog))

#iterating with keys
# for i in prog.keys():
#     val = prog[i]
#     print("key: ",i,",value = ",val, end="\n")

#iterating with items()
print("Iterate with items: \n")
for key,val in prog.items():
    print("key: ",key,",value = ",val, end="\n")







