with open('lol.txt', 'r') as firstfile, open('lol2.txt', 'a') as secondfile:
    for line in firstfile:
        secondfile.write(line)