class Olymp:
    name = ''
    mark = 0
num = int(input())
name = []
for i in range(num):
    n, m = input().split()
    m = int(m)
    olymp = Olymp()
    olymp.name = n
    olymp.mark = m
    name.append(olymp)


def binar(olymp):
    olymp.mark = -olymp.mark
    return olymp.mark
name.sort(key=binar)
for now in name:
    print(now.name)
