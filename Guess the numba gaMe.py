vPrice=float(16.90)
print("The price of a chocolate bar you want is $", vPrice, "HKD")
vCash=float(input("Enter cash amount:"))
ChangeDue= vCash-vPrice
round(ChangeDue, 2)
print("Cash imputed", vCash)
print("Change:", ChangeDue)

