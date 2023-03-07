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

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    def do_GET(self):
        if self.path == '/':
            data = db.Database('null')
            self.send_response(200)
            self.send_header('Content-type', JSON_CONTENT_TYPE)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            response = data.getDatabases()
            self.wfile.write(json.dumps(response).encode())
        elif self.path == '/data':
            print('ogga')
        else:
            print('nada get')
    def do_POST(self):
        if self.path == '/save':
            content_length = int(self.headers['Content-Length'])
            post_body = self.rfile.read(content_length)
            data = json.loads(post_body)
            database = db.Database(str(data['database']) + ".json")
            table = data['table']
            database_name = data.pop('database')
            table_name = data.pop('table')
            database.insert_data(table, data)
            self.send_response(200)
            self.send_header('Content-type', JSON_CONTENT_TYPE)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            data = {"message": "Record saved successfully"}
            self.wfile.write(json.dumps(data).encode())

        elif self.path == '/database':
            print('post')
            content_length = int(self.headers['Content-Length'])
            post_body = self.rfile.read(content_length)
            data = json.loads(post_body)
            database = db.Database(str(data['database']))
            self.send_response(200)
            self.send_header('Content-type', JSON_CONTENT_TYPE)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            data = database.getTables()
            self.wfile.write(json.dumps(data).encode())
            print('doom')
        elif self.path == '/table':
            try:

                print('post')
                content_length = int(self.headers['Content-Length'])
                post_body = self.rfile.read(content_length)
                data = json.loads(post_body)
                database = db.Database(str(data['database']))
                self.send_response(200)
                self.send_header('Content-type', JSON_CONTENT_TYPE)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                data = database.getRecords(data['table'])
                self.wfile.write(json.dumps(data).encode())
                print(data)
            except Exception as e:

                print(f"An error occurred: {e}")
        elif self.path == '/schema':
            try:

                print('post')
                content_length = int(self.headers['Content-Length'])
                post_body = self.rfile.read(content_length)
                data = json.loads(post_body)
                database = db.Database(str(data['database']))
                self.send_response(200)
                self.send_header('Content-type', JSON_CONTENT_TYPE)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                data = database.getSchema(data['table'])
                self.wfile.write(json.dumps(data).encode())
                print(data)
            except Exception as e:

                print(f"An error occurred: {e}")

        else:
            print('nada post')

PORT = 8000

httpd = http.server.HTTPServer(("", PORT), MyHandler)
print("Server serving at port", PORT)
httpd.serve_forever()