import os
from dotenv import load_dotenv
import snowflake.connector

load_dotenv()
# Configure the connections
conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA")

)

# Open a cursor
cursor=conn.cursor()

#excute the query
cursor.execute(
    """
    create table if not exists orders (
        order_id integer,
        amount integer,
        country string
    )
    """
)

# Insert the record
try :
    cursor.execute(
        """
        insert into orders (order_id,amount,country ) 
        values(%s,%s,%s)
        """,
        (3,400,'US')
    )
    print('Insert successful')
except Exception as e:
    print('Insert failed',e)
    
# select data from table
cursor.execute(
    """
    select * from orders
    """
)  
rows=cursor.fetchall()
for row in rows:
    print(row)
# Clossing the connection 
cursor.close()
conn.close()