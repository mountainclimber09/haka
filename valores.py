

class Values():
    def __init__(self, total, paid_monthlys, interests):
        self.total = total
        self.paid_monthlys = paid_monthlys
        self.interests = interests

    def well_transition(self):
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]
        j = int(total)
        intere_list = []

        for i in months:
            j = j - paid_monthly
            intere = j * interest / 100  # intere es el interes aplicado cada mes a la deuda q va quedando
            intere_list.append(intere)
            mon = round(intere / 12, 2)
            print(intere)
            print(mon)  # mon es lo q vas a pagar del interes en cada pago mensual
            final = round(1000 - mon, 2)
            print(f"Actually for {i} you are paying from those $1000.00 dollars {final} for the principal and {mon} for the interest ")  # So, if you are paying 1000 dollars every month

