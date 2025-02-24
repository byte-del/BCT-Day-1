tup=('cat','dog','goat')
list1=list(tup)
list1[1]="mice"
list1.append("cow")
tup=tuple(list1)
print(tup)
