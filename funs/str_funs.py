
# Code to run when module is run as script (not imported)
if __name__== '__main__':
    print("Running module str_funs")
else:
    print("Importing module str_funs")


def to_upper(s):
    return s.upper()
