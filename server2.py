import http.server 
import json 

class RequestHandler(http.server.BaseHTTPRequestHandler): 
	def do_GET(self): 
		if self.path == '/': 
		    self._send_json({'message': 'Welcome to the API!'},200) 
		else: 
			self._send_json({'error': 'Not found'}, 404) 

	def do_POST(self): 
		if self.path == '/data': 
			if self._check_auth(): 
				length = int(self.headers['Content-Length']) 
				data = json.loads(self.rfile.read(length)) 
				# record data in database 
				self._send_json({'message': 'Data recorded successfully!'}) 
			else: 
				self._send_json({'error': 'Unauthorized access'}, 401) 
		else: 
			self._send_json({'error': 'Not found'}, 404) 

	def _send_json(self, data, status=200): 
		self.send_response(status) 
		self.send_header('Content-type', 'application/json') 
		self.end_headers() 
		self.wfile.write(bytes(json.dumps(data), 'utf-8')) 

	def _check_auth(self): 
		if 'Authorization' not in self.headers: 
			return False 
		auth = self.headers['Authorization'].split(' ')[1] 
		username, password = auth.decode('base64').split(':') 
		return username == 'admin' and password == 'password' 

if __name__ == '__main__': 
	server = http.server.HTTPServer(('', 8000), RequestHandler) 
	server.serve_forever()