import snowflake.connector

# Configure the connections
conn=snowflake.connector.connect(
    user='birdlover',   
    password='Snowflake_2026',
    account='uk83621.me-central-1.aws',
    warehouse='COMPUTE_WH',
    database='demo_db',
    schema='PUBLIC'
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