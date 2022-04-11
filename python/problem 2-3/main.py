import random as rand
i = 1
j = 1
k = 1
m = 1
number_list = []
while i <= 100:
    rand_number = rand.randrange(100)
    number_list.append(rand_number)
    i += 1
number_list.sort()
many_list = number_list.copy()
cleaning_list = number_list.copy()
clean_list = []
checking_number = 999999
checking_time = 0
many_time = 1
many_number = []
first_max_number = 0
second_max_number = 0
third_max_number = 0
while j <= 100:
    if checking_number != many_list[0]:
        if checking_time == many_time:
            many_number.append(checking_number)
        elif checking_time > many_time:
            many_time = checking_time
            many_number.clear()
            many_number.append(checking_number)
        checking_number = many_list[0]
        checking_time = 0
        checking_time += 1
        many_list.pop(0)
    elif checking_number == many_list[0]:
        checking_time += 1
        many_list.pop(0)
    j += 1
while k <= 99:
    if cleaning_list[0] == cleaning_list[1]:
        cleaning_list.pop(0)
    elif cleaning_list[0] != cleaning_list[1]:
        clean_list.append(cleaning_list[0])
        cleaning_list.pop(0)
    k += 1
if cleaning_list[0] != clean_list[-1]:
    clean_list.append(cleaning_list[0])
many_number = ','.join(str(s) for s in many_number)
print("최고 중복 수는 "+many_number+" 입니다. 중복횟수는 %d 입니다." % many_time)
print("세번째 최고 수는 %d입니다" % clean_list[-3])
print(clean_list)
