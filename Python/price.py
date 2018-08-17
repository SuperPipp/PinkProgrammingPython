string = input("What was the price of your meal?")
price = int(string)
if price > 100:
    x = price*0.05
    print(x)
else:
    y = price*0.10
    print(y)