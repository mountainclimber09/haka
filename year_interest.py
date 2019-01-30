months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
inter_list = []


def per_year(value, paid_monthly, interest):
  j = int(value)
  for i in months:
    j = j-paid_monthly
    intere = j*interest/100 #intere es el interes aplicado cada mes a la deuda q va quedando
    inter_list.append(intere)
    mon = round(intere/12, 2)
    print(intere)
    print(mon)  #mon es lo q vas a pagar del interes en cada pago mensual
    final = round(1000-mon, 2)
    print(f"Actually for {i} you are paying from those $1000.00 dollars {final} for the principal and {mon} for the interest ") #So, if you are paying 1000 dollars every month


def new_total_interest(value, paid_monthly, interest):
    interest_remaining = inter_list[11]
    if interest_remaining > 0:
        new_value = value + interest_remaining - paid_monthly
        inter_of_amount_on_year = new_value * interest / 100
        print(inter_of_amount_on_year)
        print(f"New amount to pay is: {value+interest_remaining}")

    if value+interest_remaining > value:
        print("\n\nDon't try to do this while you can't pay more to your debt." '\nPlease increase your monthly payment')
    else:
        print("\n\nYour payment is enough to kill your debts")


per_year(25000, 2100, 23)
print(inter_list)

new_total_interest(25000, 2100, 23)




#Tengo q buscar la via de q si el usuario quiere reducir sus pagos, tratar de q ningun mes quede en negativo tratando de optimizarlo