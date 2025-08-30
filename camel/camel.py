def main():

    name = input("camelCase: ")

    for i in name:
        if i.isupper():
            name = name.replace(i, f"_{i.lower()}")

    print(f"snake_case: {name}")

main()