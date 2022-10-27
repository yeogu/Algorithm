expression = input()
number = []
operation = []

# parsing
temp = ""
for i in range(len(expression)):
    value = expression[i]
    if value == "+" or value == "-":
        operation.append(value)
        if temp != "":
            number.append(int(temp))
        temp = ""
    else:
        temp += expression[i]
if temp != "":
    number.append(int(temp))

# bracket
result = number[0]
bMinus = False

for i in range(1, len(number)):
    oper = operation[i-1]
    if oper == "+":
        if bMinus is False:
            result += number[i]
        else:
            result -= number[i]
    elif oper == "-":
        if bMinus is False:
            bMinus = True
        result -= number[i]

print(result)