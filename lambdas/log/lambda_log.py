#Import library

import boto3 as b3
import json as js
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine


'''
client = b3.client('lambda', region_name='us-east-1')


event = {
	"id1":"2023-20-23"
}

response = client.invoke(
    FunctionName='motivy-analytics-lambdas-LogLambda-ebhzDjXd2E9M',
    Payload=js.dumps(event)
)

result = js.loads(response['Payload'].read())
print(result)

print("End of excecution")
'''
def lambda_handler(event, context):
    # TODO implement
    '''
	De next steps in order to excecute this lambda is to 
	import the boto library, contect to the rsd wharehouse 
	with the corresponding aws access keys/secrets and variables to finally test
	the conexion executing a query
    '''
    '''
    # Set up the connection parameters
     db_username = 'your_db_username'
     db_password = 'your_db_password'
     db_host = 'your_redshift_cluster_endpoint'
     db_port = 5439
     db_name = 'your_database_name'

     # Construct the connection string
     conn_string = f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'

     # Create the SQLAlchemy engine
     engine = create_engine(conn_string)

     # Execute a sample query
     with engine.connect() as conn:
        result = conn.execute('SELECT COUNT(*) FROM your_table')
        count = result.fetchone()[0]
        print(f'Total rows in table: {count}')
    '''
    # Set up the connection parameters
    conn = psycopg2.connect(
    	host='motivy-redshift-cluster.cxrt7addrmk7.us-east-1.redshift.amazonaws.com',
	port=5439,
	dbname='dev',
	user='rdsamin',
	password='A0so%33r7Jf6'
    )
 
    # Construct the connection string
    cur = conn.cursor()
    cur.execute("select * from exec_time et")
    rows = cur.fetchall()

    # Execute a sample query
    '''
    cur.execute("INSERT INTO mytable (id, name, age) VALUES (%s, %s, %s)", (1, 'John Doe', 30))
    with open('data.csv', 'r') as f:
	 cur.copy_expert('COPY mytable FROM STDIN WITH CSV HEADER', f)
    conn.commit()
    '''
    print(rows)

    cur.close()
    conn.close()
    message = "Hello, world!"
    return message

event = {
   "key1":"value1"
 }
lambda_handler(event,None)
