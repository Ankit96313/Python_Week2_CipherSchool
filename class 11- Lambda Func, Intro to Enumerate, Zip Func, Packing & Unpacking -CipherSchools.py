lambda a,b:a+b
names=["Ankit","Vishal","Cipher School"]
for name in names:
    print(name)
    
    
a=5
b=9
temp=a
a=b
b=temp


a=5
b=9
a,b=b,a
print(a,b)


names=["Ankit","Vishal","Cipher School"]
scores=[50,80.90,70]
states=["Bihar","Uttar Pradesh","Punjab"]
for a in  names,scores,states in zip(names,scores,states):
    print(name,"_",scores,states)

    

