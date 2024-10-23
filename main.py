with open("text.txt", "r") as file: 
    s = file.read() 
s = s.replace('o', 'a') 
with open("output.txt", "w+") as file: 
    file.write(s) 