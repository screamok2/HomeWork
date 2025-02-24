time = int(input("input the number 0-8640000:"))
if time >= 8640000:
    time = 8640000
minutes, secunds = divmod(time, 60)
secunds1 = str(secunds).zfill(2)
hours, minutes1= divmod(minutes, 60)
minutes2 = str(minutes1).zfill(2)
days, hours1 = divmod(hours, 24)
hours2 = str(hours1).zfill(2)
days1 =days % 10
if days1 == 1 :
    days2 = "день"
elif days1 in (2,3,4):
    days2 = "дні"
elif days1 in (5,6,7,8,9,0):
    days2 = "днів"
if days % 100 in (11,12,13,14,15,17,18,19):
    days2 = "днів"
print(f"{days} {days2} , {hours2}:{minutes2}:{secunds1}")
