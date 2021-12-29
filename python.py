print("Hello world")
# 引数内で文字指定

print('''<h1>hello world</h1>"
<p>世界の皆さん,
<h1>hello world</h1>''')


# 変数
player = "勇者"
print(player)
print(player + "荒野を歩いていた")
print(player + "モンスターと戦った")
print(player + "モンスターを倒した")

# サイコロ
import random
number = random.randint(10,100)
print("スライムが" + str(number) + "匹現れた")

# 演算子
num = 100 % 20 + 230
print(num + 100)
print(num + num)
print(num)

# りんごの単価
# りんごを買う数  合計金額と自腹割合を出してみた
import random
apple_price = random.randint(1,3) * 100
apple_num = random.randint(1,10)
print("りんごの単価" + str(apple_price) + "円")
print("りんごの単価" + str(apple_num) + "個")
total = apple_price * apple_num
print("合計金額：" + str(total) + "円")
charge = 0.5 * 10
print("私の負担割合は" + str(charge) + "割です")
my_total = total * (charge / 10)
print("自腹の金額は"+ str(my_total) + "円です")
