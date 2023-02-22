import http.server
import json
import re
import Database as db

WRITE_PATH = '/write'
READ_PATH = '/read'
JSON_CONTENT_TYPE = 'application/json'

class MyHandler(http.server.BaseHTTPRequestHandler):


    def getnumberfrom_route(self):
        regex = r'^.*/(\d+)$'
        match = re.match(regex, self.path)
        if match is not None:
            return int(match.group(1))
        else:
            return None

    def do_GET(self):
        index = self.getnumberfrom_route()
        index = None if index is None else index+1
        print('None' if index is None else index)
        if(index):
            index=index-1
            print(self.path.replace('/'+str(index),''))
            if self.path.replace('/'+str(index),'') == '/read':
                i = 1
                with open('file.json', 'r') as f:
                        data = json.load(f)
                print(data)  
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                if len(data['patients']) > 0 and 0 <= index < len(data['patients']):
                    self.wfile.write(bytes(json.dumps(data['patients'][index]), 'utf-8'))
                else:
                    self.wfile.write(bytes('{"message":"invalid index"}', 'utf-8'))
            else:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(bytes('{"message":"invalid format"}', 'utf-8'))
            
        elif self.path == '/read' or self.path == '/read/':
            with open('file.json', 'r') as f:
                data = json.load(f)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(data), 'utf-8'))
        else:
            self.send_response(404)
            self.end_headers()



    def do_POST(self):
        # Merge nested if conditions
        if self.path != WRITE_PATH:
            self.send_response(404)
            self.end_headers()
            return

        # Hoist duplicate code out of conditionals


        content_length = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_length)
        data = json.loads(post_body)

        # Extract method for saving data to file


        database = db.Database(str(data['database']) + ".json")
        table = data['table']

        # Use dictionary pop method to remove keys and get values
        database_name = data.pop('database')
        table_name = data.pop('table')

        database.insert_data(table, data)

        self.send_response(200)
        self.send_header('Content-type', JSON_CONTENT_TYPE)
        self.end_headers()
        data = {"message": "Record saved successfully"}
        self.wfile.write(json.dumps(data).encode())

PORT = 8080

httpd = http.server.HTTPServer(("", PORT), MyHandler)
print("Server serving at port", PORT)
httpd.serve_forever()