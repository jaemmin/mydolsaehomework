money = int(input("금액을 입력하세요: "))
while True:
    if money >= 99999:
        money = int(input("금액을 입력하세요: "))
    elif money < 10000:
        money = int(input("금액을 입력하세요: "))
    else:
        break
money_first = money // 10000
money = money - 10000 * money_first
money_second = money // 1000
money = money - 1000 * money_second
money_third = money // 100
money = money - 100 * money_third
money_fourth = money // 10
money = money - 10 * money_fourth
money_fifth = money
if money_second==0:
    print("%d만 %d백 %d십 %d원" % (money_first, money_third, money_fourth, money_fifth))
elif money_third==0:
    print("%d만 %d천 %d십 %d원" % (money_first, money_second, money_fourth, money_fifth))
elif money_fourth==0:
    print("%d만 %d천 %d백 %d원" % (money_first, money_second, money_third, money_fifth))
elif money_fifth==0:
    print("%d만 %d천 %d백 %d십원" % (money_first, money_second, money_third, money_fourth))
else:
     print("%d만 %d천 %d백 %d십 %d원" % (money_first, money_second, money_third, money_fourth, money_fifth))

