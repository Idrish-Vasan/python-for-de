import csv
rows = [
    ['order_id','customer','amount','country'],
    [1,'Alice',120.5,'US'],
    [2,'Bob',75.0,'IN'],
    [3,'Charlie',200.0,'US']
]

# Writing to a CSV file
'''
with open('orders.csv','w',newline='') as f:
    writer=csv.writer(f)
    writer.writerows(rows)
    '''
    
# Reading from a CSV file
with open('orders.csv','r') as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)  