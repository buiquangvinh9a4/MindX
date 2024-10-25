with open('matran.inp', 'r') as file:
    s = file.readline()
    s = s.split()
    for line in file:
        print(line)