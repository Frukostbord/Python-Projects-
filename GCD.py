def divide_text():
    uppslag = {}
    text = "Hej där där där där där underbara barn! barn! barn! Hur mår du idag?"
    text = text.lower() #lower case
    text = text.split() #creating a list
    text.sort()
    for i in text: #for loop
        complete_text = i.strip(", .?!") #removes characters
        uppslag[complete_text] = text.count(i) #creates a dictionary
    return uppslag


def counting_size(): #Creating a dictionary only containing words with 2 or more occurrences
    x = divide_text()
    new_uppslag = dict()
    for j, k in x.items():
        if k > 1:
            new_uppslag[j] = k
    return new_uppslag

def main():
    x = counting_size()
    print(x)

main()

