# Kilometer to mile converter


print("How many Km do you want to convert?")

Km = input() #or Km  = float(input())
Km = float(Km)
mile = Km / 1.60934 #or mile = float(Km) / 1.60934
mile = round(mile, 2)
print(f"{Km} Km is {mile} mile")