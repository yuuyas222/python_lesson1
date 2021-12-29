import random
test = input("この買い物に何割負担してくれますか: ")
test = int(test)
apple_price = random.randint(1,3) * 100
apple_num = random.randint(1,10)
print("りんごの単価" + str(apple_price) + "円")
print("りんごの単価" + str(apple_num) + "個")
total = apple_price * apple_num
print("合計金額：" + str(total) + "円")
charge = test 
print("私の負担割合は" + str(charge) + "割です")
my_total = total * (charge / 10)
print("自腹の金額は"+ str(my_total) + "円です")