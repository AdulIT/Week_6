fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
File = fin.readlines()
File.sort()
for line in File:
    print(*line.split()[:2] + line.split()[3:], file=fout)
fin.close()
fout.close()
