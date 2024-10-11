input_data = open("input.txt","r")
data = input_data.read()
data = data.split()
a = int(data[0])
b = int(data[1])
c = int(data[2])
d = 0
if (a >= b) and (a >= c):
    d = a
elif (b >= a) and (b >= c):
    d = b
elif (c >= a) and (c >= b):
    d = c 
d = str(d)    
output_data = open("output.txt","w")
output_data.write (d)
input_data.close()
output_data.close()     