#Import library

import pymysql.cursors

def lambda_handler(event, contect):
    # TODO implement
    '''
	De next steps in order to excecute this lambda is to 
	import the boto library, contect to the rsd wharehouse 
	with the corresponding aws access keys/secrets and variables to finally test
	the conexion executing a query
    '''

    # Set up the connection parameters
    conn = pymysql.connect(
    	host='motivy-redshift-cluster.cxrt7addrmk7.us-east-1.redshift.amazonaws.com',
	port=5439,
	dbname='dev',
	user='rdsamin',
	password='A0so%33r7Jf6',
	cursorclass=pymysql.cursors.DictCursor
    )

    conn.close()

    message = "Hello, world!"
    return message

#event = {
#   "key1":"value1"
# }
#lambda_handler(event,None)
