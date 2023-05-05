#Import library

import psycopg2

HOST = 'motivy-redshift-cluster.cxrt7addrmk7.us-east-1.redshift.amazonaws.com'
USER = 'rdsamin'
PASSWORD = 'A0so%33r7Jf6'
PORT = 5439
DBNAME = 'dev'

def get_redshift_con(password=PASSWORD,
                     user=USER,
                     host=HOST,
                     port=PORT,
                     dbname=DBNAME):
    return psycopg2.connect(dbname=dbname,host=host,port=port,user=user,password=password)

def lambda_handler(event, context):
    # TODO implement
    '''
	De next steps in order to excecute this lambda is to 
	import the boto library, contect to the rsd wharehouse 
	with the corresponding aws access keys/secrets and variables to finally test
	the conexion executing a query
    '''

    # Set up the connection parameters
    print(f'Create Conexion')
    conn = get_redshift_con()
    print(f'Conexion Succeded')

   
    # Set up the cursor and excecute query
    print(f'Create Cursor Query')
    cur = conn.cursor()
    query = 'SELECT * FROM exec_time e'
    print(query)	

    print(f'Excecute Query')
    cur.execute(query)
    print(cur.fetchall())

    print(f'Committing changes')
    conn.commit()

    print(f'Closing Connection')
    cur.close()
    conn.close()

    message = "Eof"
    print(message)

    return "Exited with status code 200"+message

#event = {
#   "key1":"value1"
# }
#lambda_handler(event,None)
