import csv

class DataPipeline:
    def __init__(self,source,destination):
        self.source=source
        self.destination=destination
    
    # Extraction of the data
    def extract_data(self):
        print(f'Extracting data from {self.source}')
        data=[]
    
        with open(self.source,newline='',encoding='utf-8') as csvfile:
            reader=csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
            return data
    
    # Transformation of the data
    def transforming_data(self,data):
        print('Transforming the data :')
        cleaned_data=[]
        
        for row in data :
            if row['amount'] not in [None,"","NULL",'null']:
                row['amount']=float(row['amount'])
                cleaned_data.append(row) 
                
        return cleaned_data
    
    # Load the data into destination
    def load_data(self,data):
        print(f'loading {len(data)} records to {self.destination}')
        
        if not data:
            print('No data to write')
            return
        
        with open(self.destination,'w',newline="",encoding='utf-8') as csvfile:
            writer=csv.DictWriter(csvfile,fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data )
            
    # Orchestrate Flow
    def run(self):
        data=self.extract_data()
        data=self.transforming_data(data)
        self.load_data(data)

pipeline=DataPipeline('dirty_orders.csv','clean_orders.csv')
pipeline.run()