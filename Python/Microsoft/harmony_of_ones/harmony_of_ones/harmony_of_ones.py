entries = input("Number of entries");
inputs = []
output = [];
for i in range(int(entries)):
    inputs.append(input("x,y: ").split(","));
    inputs[i][0] = bin(int(inputs[i][0]));
    inputs[i][1] = bin(int(inputs[i][1]));
    output.append(0);
    first_len = len(inputs[i][0]) - 1;
    second_len= len(inputs[i][1]) - 1;
    min_len = (first_len if first_len<=second_len else second_len)
    for j in range(min_len):
        if inputs[i][0][first_len - j] == inputs[i][1][second_len - j] and inputs[i][0][first_len - j] == "1":
            output[i] += 1;
for c in output:
    print(c);
    

