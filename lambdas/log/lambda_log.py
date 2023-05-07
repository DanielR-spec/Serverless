# Import library
import redshift_connector
import json
import os

HOST = os.environ['DBHost']
USERNAME = os.environ['DBUser']
PASSWORD = os.environ['DBPassword']
PORT = os.environ['DBPort']
DBNAME = os.environ['DBName']

def get_redshift_con(password=PASSWORD,
                     user=USERNAME,
                     host=HOST,
                     port=PORT,
                     dbname=DBNAME):
    return redshift_connector.connect(database=dbname,host=host,port=port,user=user,password=password)


def lambda_handler(event, context):
    # TODO implement

    # Parse out query strin params
    transactionId = event['queryStringParameters']['transactionId']
    transactionType = event['queryStringParameters']['type']
    transactionAmount = event['queryStringParameters']['amount']

    #print(transactionId)
    #print(transactionType)
    #print(transactionAmount)

    # Construct the body of the response object
    transactionResponse = {}
    transactionResponse['transactionId'] = transactionId
    transactionResponse['type'] = transactionType
    transactionResponse['amount'] = transactionAmount
   
 
    # Construct http resoinse object
    responseObject = {}

    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'

    
    # Create connection with RDS Cluster
    conn = get_redshift_con()

    # Set up the cursor and excecute query
    cursor: redshift_connector.Cursor = conn.cursor()
    query = 'SELECT * FROM exec_time e'
    cursor.execute(query)
    row = cursor.fetchall()

    # Commit changes if any
    conn.commit()

    # Close cursor index & connection
    cursor.close()
    conn.close()

    res = str(row)
   # return "Exited with status code 200.\n- DataBase respondes with:\n"+"-"+res

   # print(responseObject)
    transactionResponse['message'] = 'Exited with satatus code 200. res: ' + res
    responseObject['body'] = json.dumps(transactionResponse)
    return responseObject

#event = {
#   'queryStringParameters':{
#	'transactionId':1,
#	'type':'HTTP/1',
#        'amount':128	
#	}
# }
#lambda_handler(event,None)
