uspeh = float(input("Enter uspeh: "))
MaxStip = int(input("Vyvedete max stipendiq: "))
if uspeh >= 5.50:
    print("Max stipendiq", MaxStip)
elif 5.50 > uspeh >= 5.00:
    print("70% ot Max stipendiq", MaxStip * 0,7)
elif 5.00 > uspeh >= 4.50:
    print("50% ot Max stipendiq", MaxStip * 0,5)
else:
    print("Ne poluchava stipendiq.")
