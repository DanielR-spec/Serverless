# Import library
import redshift_connector
import json
import sys, os

HOST = os.environ['DBHost']
USERNAME = os.environ['DBUser']
PASSWORD = os.environ['DBPassword']
PORT = int(os.environ['DBPort'])
DBNAME = os.environ['DBName']

def get_redshift_con(password=PASSWORD,
                     user=USERNAME,
                     host=HOST,
                     port=PORT,
                     dbname=DBNAME):
    return redshift_connector.connect(database=dbname,host=host,port=port,user=user,password=password)


def lambda_handler(event, context):

    # TODO implement

    try:

    # Caputer request event

        http_method = event['httpMethod']

    # Construct Object & the body of the response

        transactionResponse = {}
        responseObject = {}

    # Review request type and return acording response

        if http_method == 'GET':

    # Construct http response object

            transactionResponse['message'] = 'Hello from HTTP GET!'

            responseObject['statusCode'] = 200
            responseObject['headers'] = {}
            responseObject['headers']['Content-Type'] = \
                'application/json'
            responseObject['body'] = json.dumps(transactionResponse)
        elif http_method == 'POST':

        # Construct http response object

            body = json.loads(event['body'])
            transactionResponse['message'] = 'Hello from HTTP POST!'

            responseObject['statusCode'] = 200
            responseObject['headers'] = {}
            responseObject['headers']['Content-Type'] = \
                'application/json'
            responseObject['body'] = json.dumps(transactionResponse)
            responseObject['data'] = body
        else:

            if event is not None:

            # Local Testing

                body = event['body']
                transactionResponse['message'] = \
                    'Hello from Local Lambda!'

                responseObject['statusCode'] = 200
                responseObject['headers'] = {}
                responseObject['headers']['Content-Type'] = \
                    'application/json'
                responseObject['body'] = json.dumps(transactionResponse)
                responseObject['data'] = body
            else:

        # Error Handling

                transactionResponse['message'] = \
                    'Bad Request, Invalid Lambda Invocation!'

                responseObject['statusCode'] = 400
                responseObject['headers'] = {}
                responseObject['headers']['Content-Type'] = \
                    'application/json'
                responseObject['body'] = json.dumps(transactionResponse)

        #print(responseObject)
        return responseObject
    except Exception as e:
        line = str(e)
        #print(exc_type, fname, exc_tb.tb_lineno)
        return 'Exited with status code 401: service not found' + line

#event = {
#   'httpMethod':'LOCAL',
#   'body':{
#	'transactionId':1,
#	'type':'HTTP/1',
#        'amount':128
#	}
# } 
#lambda_handler(event,None)
