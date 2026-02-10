import json
data={
    'orders':[
        {'id':1,'items':[{'sku':'A1','qty':2}]},
        {'id':2,'items':[{'sku':'B2','qty':1}]},
        {'id':3,'items':[{'sku':'C3','qty':3}]}
    ]
}
# Writing to a JSON file
'''
with open('orders.json','w') as f:
    json.dump(data,f,indent=4)
    '''
    
# Reading from a JSON file
with open('orders.json','r') as f:
    loaded_data=json.load(f)
    # for data in loaded_data['orders']:
    #     print(data)
rows=[]
for order in loaded_data['orders']:
    for item in order['items']:
        rows.append({
            'order_id':order['id'],
            'sku':item['sku'],
            'quantity':item['qty']
        })
        
print(rows)