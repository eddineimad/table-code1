def soutable(T,a,b):
    tab1 = []
    for i in range(a,b):
        tab1.append(T[i])
    return tab1

tab = []
for i in range(10):
    print("enter the element number",i+1,":")
    A = int(input())
    tab.append(A)
a = int(input("enter the first index :"))
b = int(input("enter the second index :"))
print(soutable(tab,a,b))