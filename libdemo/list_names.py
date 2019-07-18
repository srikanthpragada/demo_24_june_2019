with open("names.txt", "r") as f:
    for lineno, name in enumerate(f,start=1):
        print(f"{lineno:3} : {name}", end='')


