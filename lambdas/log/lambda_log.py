#Import library

import redshift_connector


HOST = 'motivy-redshift-cluster.cxrt7addrmk7.us-east-1.redshift.amazonaws.com'
USERNAME = 'rdsamin'
PASSWORD = 'A0so%33r7Jf6'
PORT = 5439
DBNAME = 'dev'

def get_redshift_con(password=PASSWORD,
                     user=USERNAME,
                     host=HOST,
                     port=PORT,
                     dbname=DBNAME):
    return redshift_connector.connect(database=dbname,host=host,port=port,user=user,password=password)


def lambda_handler(event, context):
    # TODO implement

    #Create connection with RDS Cluster
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
    return "Exited with status code 200.\n- DataBase respondes with:\n"+"-"+res

#event = {
#   "key1":"value1"
# }
#lambda_handler(event,None)
