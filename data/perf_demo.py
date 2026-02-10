import time
import pandas as pd
import numpy as np

# Create DataFrame
df=pd.DataFrame({
    "amount":np.random.randint(1,1000,size=1_000_000)
})

#Slow way : Loop
start=time.time()

total=0
for val in df['amount']:
    total+=val

print('Loop sum :',total)
print('Time taken :',time.time()-start)

# Fast Way :Vectorized
start=time.time()

total=df['amount'].sum()
end=time.time()
print('Vectorized Sum :',total)
print('Time taken is :',end-start) 