from datetime import datetime

# Visar dagensdatum (år,månad,dag) samt tid i timme, minut, samt sekund
print(datetime.now())

month = datetime.now().month

#denna kod nedan hämtar vilken månad det är (1 = Januari, 2 = Februari, etc).
#koden skriver även ut den nuvarande månaden, samt månadens namn
if(month == 1):
    print("Nuvarande månad: Januari")
elif(month == 2):
    print("Nuvarande månad: Februari")
elif(month == 3):
    print("Nuvarande månad: Mars")
elif(month == 4):
    print("Nuvarande månad: April")
elif(month == 5):
    print("Nuvarande månad: Maj")
elif(month == 6):
    print("Nuvarande månad: Juni")
elif(month == 7):
    print("Nuvarande månad: Juli")
elif(month == 8):
    print("Nuvarande månad: Augusti")
elif(month == 9):
    print("Nuvarande månad: September")
elif(month == 10):
    print("Nuvarande månad: Oktober")
elif(month == 11):
    print("Nuvarande månad: November")
elif(month == 12):
    print("Nuvarande månad: December")