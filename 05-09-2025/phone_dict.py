n=int(input("Enter limit"))
m={}
mob=0
name=""
i=0
for i in range (0,n):
    mob=int(input("enter mobile number"))
    name=str(input("enter name"))
    z2=dict({mob:name})
    m.update (z2)
print(m)
n-int(input("enter the no to search in dictionary"))
print("the name of personis ",m[n]) 
