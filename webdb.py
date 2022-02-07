import os
import psycopg2
#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='diego00', host='db', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()
#Executing an MYSQL function using the execute() method
cursor.execute("select version()")
# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)
#Closing the connection
conn.close()
from http.server import HTTPServer, CGIHTTPRequestHandler
os.chdir('.')
SPORT=os.getenv('LPORT')
LPORT=int(SPORT)
#print (LPORT)
server_object = HTTPServer(server_address=('', LPORT), RequestHandlerClass=CGIHTTPRequestHandler)
server_object.serve_forever()
