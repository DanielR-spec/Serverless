
import pandas as pd
import json
def lambda_handler(event, context):
    message = "Hello, world!"
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
