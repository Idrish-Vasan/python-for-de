def calculate_total(order):
    if 'amount' not in order:
        raise ValueError("Missing 'amount' in order")
    return order['amount'] * 2

order={
    'amunt': 100
}
total=calculate_total(order)
print(f'Total amount: {total}')

