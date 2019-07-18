f = open("salaries.txt", "rt")

for line in f:
    parts = line.strip("\n").split(",")
    if len(parts) < 2:
        continue

    name = parts[0]
    salaries = [int(v) for v in parts[1:] if v.isdigit()]
    avg = sum(salaries) / len(salaries)
    print(f"{name:10} {avg}")
