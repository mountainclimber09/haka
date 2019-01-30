def interest_financed(value):

    interest_total = int(0)
    for i in value:
        interest_total = interest_total + i

    print(f"The total interest in x years is {interest_total}")
