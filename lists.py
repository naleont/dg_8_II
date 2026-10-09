groceries_list = ['колбаса', 'хлеб']
inp = input()
new = inp.split(',')
groceries_list.extend(new)
print(groceries_list)
print(len(groceries_list))