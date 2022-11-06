T = int(input())

for t in range(T):
    price = 0
    a, b = map(int, input().split())
    if a == 1:
        price += 5000000
    elif 2 <= a and a <= 3:
        price += 3000000
    elif 4 <= a and a <= 6:
        price += 2000000
    elif 7 <= a and a <= 10:
        price += 500000
    elif 11 <= a and a <= 15:
        price += 300000
    elif 16 <= a and a <= 21:
        price += 100000
    
    if b == 1:
        price += 5120000
    elif 2 <= b and b <= 3:
        price += 2560000
    elif 4 <= b and b <= 7:
        price += 1280000
    elif 8 <= b and b <= 15:
        price += 640000
    elif 16 <= b and b <= 31:
        price += 320000
    
    print(price)