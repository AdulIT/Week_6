def CountSort(a):
    for now in myList:
        grades[now] += 1
    for grade in range(len(grades)):
        for i in range(grades[grade]):
            print(grade, end=' ')
myList = list(map(int, input().split()))
grades = [0] * 101
CountSort(myList)
