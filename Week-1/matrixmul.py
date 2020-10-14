print("Enter the values of matrix 1: ")
x = []
y = []
for i in range(3):          
    a =[] 
    for j in range(3):      
         a.append(int(input())) 
    x.append(a)

print("Enter the values of matrix 2: ")
for i in range(3):          
    b =[] 
    for j in range(3):      
         b.append(int(input())) 
    y.append(b)  
 
result = [[0,0,0],  
          [0,0,0],  
          [0,0,0]]  

for i in range(len(x)):  
       for j in range(len(y[0])):  
           for k in range(len(y)):  
               result[i][j] += x[i][k] * y[k][j]  
for r in result:  
   print(r)  
