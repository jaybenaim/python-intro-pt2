temp = input("Pick a farenheit to convert!\n")
temp = int(temp) 

def convert(num): 
    return (num - 32) * 5/9 

print("The temperature in celcius is {:.2f}".format(convert(temp)))
