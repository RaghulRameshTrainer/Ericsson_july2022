from bank import Account

acc=Account('Raghul Ramesh','ALRTE5766R',10000)
print(acc.NAME)
print(acc.password)
# print(acc.getAmount())
# acc.setAmount(100000)
# print(acc.getAmount())

print(acc.__amount)
acc.__amount=1000000
print(acc.__amount)
