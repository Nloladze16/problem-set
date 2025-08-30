def main():
    text = input("Input: ")

    vovels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    for i in vovels:
        text = text.replace(i, "")

    print(f"Output: {text}")


main()
