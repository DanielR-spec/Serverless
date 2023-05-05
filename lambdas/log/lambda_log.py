#Import library

import pymysql

HOST = 'motivy-redshift-cluster.cxrt7addrmk7.us-east-1.redshift.amazonaws.com'
USERNAME = 'rdsamin'
PASSWORD = 'A0so%33r7Jf6'
PORT = 5439
DBNAME = 'dev'

connection = pymysql.connect(host=HOST,
			     port=PORT,
			     user=USERNAME,
                             password=PASSWORD,
                             database=DBNAME)

def lambda_handler(event, context):
    # TODO implement
    '''
	De next steps in order to excecute this lambda is to 
	import the boto library, contect to the rsd wharehouse 
	with the corresponding aws access keys/secrets and variables to finally test
	the conexion executing a query
    '''

   
    # Set up the cursor and excecute query
    print(f'Create Cursor Query')
    cursor = connection.cursor()
    query = 'SELECT * FROM exec_time e'
    print(query)	

    print(f'Excecute Query')
    cursor.execute(query)
    print(cursor.fetchall())

    print(f'Committing changes')
    connection.commit()

    print(f'Closing Connection')
    cursor.close()
    connection.close()

    message = "Eof"
    print(message)

    return "Exited with status code 200"

#event = {
#   "key1":"value1"
# }
#lambda_handler(event,None)
