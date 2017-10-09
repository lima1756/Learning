import re;

paths = [];
output = []
with open("test.txt") as f:
    paths = f.readlines()
i = 0;
for p in paths:
    directories = p.split("\\");
    c = 0;
    output.append("");
    directories[len(directories)-1] = directories[len(directories)-1].replace("\n", "");
    while c < len(directories):
        if c == -1:
            c = 0;
        if directories[c] == "*":
            directories = directories[c+1:];
            c = -1;
        if re.fullmatch("\.+", directories[c]):
            cantidad = directories[c].count(".") - 1;            
            if cantidad < (c + 1):
                directories = directories[0:c-cantidad] + directories[c+1:]
            else:
                directories = directories[c+1:]
            c = -1; 
        c+=1;
        output[i] = directories;
    i += 1;
for x in output:
    print(x);