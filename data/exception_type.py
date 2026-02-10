try:
    amount='100'
    total=200 + amount
except TypeError:
    amount=int('100')
    total=amount+30 
    print(total)