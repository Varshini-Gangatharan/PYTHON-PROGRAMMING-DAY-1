fresh_loaves=int(input("Enter the number of fresh loaves purchased: "))
day_old_loaves=int(input("Enter the number of day old loaves purchased: "))
regular_price=185.00
print("Regular price: Rs.",regular_price)
day_old_loaves_price=regular_price*0.4*day_old_loaves
fresh_loaves_price=regular_price*fresh_loaves
total_price=day_old_loaves_price+fresh_loaves_price
print("Amount of new loaves: ",fresh_loaves_price)
print("Amount of day old loaves: ",day_old_loaves_price)
print("Total amount: ",total_price)
