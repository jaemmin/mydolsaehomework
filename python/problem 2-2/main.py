number = int(input("숫자를 입력하세요: "))
measure = []
i = 1
while i <= number:
    if number % i == 0:
        measure.append(i)
        i += 1
    else:
        i += 1
print(measure)