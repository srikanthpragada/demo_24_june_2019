# Print common chars in two strings

st1 = input("First string  : ")
st2 = input("Second string : ")

for c in st1:
    if c in st2:
        print(c)


