def main():

    greeting = input("Greeting: ").lower().strip()

    greet = greeting[0:5]

    if greeting[0] == "h":
        # if greeting[1] == "e" and greeting[2] == "l" and greeting[3] == "l" and greeting[4] == "o":
        if greet == "hello":
            print("$0")
        else :
            print("$20") 
    else :
        print("$100")

main()                 

