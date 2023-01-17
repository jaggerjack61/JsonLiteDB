
import json 
from flask import Flask, request, jsonify 

app = Flask(__name__) 

@app.route('/database', methods = ['POST']) 
def create_database(): 
	data = request.json 
	with open('database.txt', 'w') as outfile: 
		json.dump(data, outfile) 
	return jsonify({'message': 'Database created successfully!'}), 200 

@app.route('/database/<string:name>', methods = ['GET']) 
def get_data(name): 
	with open('database.txt') as json_file: 
		data = json.load(json_file) 
		user = data.get(name) 
	if user: 
		return jsonify(user), 200 
	else: 
		return jsonify({'message': 'User not found!'}) 

@app.route('/database/<string:name>', methods = ['PUT']) 
def update_data(name): 
	data = request.json 
	with open('database.txt') as json_file: 
		json_data = json.load(json_file) 
	if name in json_data: 
		json_data[name] = data 
		with open('database.txt', 'w') as outfile: 
			json.dump(json_data, outfile) 
		return jsonify({'message': 'User updated successfully!'}), 200 
	else: 
		return jsonify({'message': 'User not found!'}) 

@app.route('/database/<string:name>', methods = ['DELETE']) 
def delete_data(name): 
	with open('database.txt') as json_file: 
		json_data = json.load(json_file) 
		if name in json_data: 
			del
            with open('database.txt', 'w') as outfile: 
			json.dump(json_data, outfile)
		return jsonify({'message': 'User deleted successfully!'}), 200 
	else: 
		return jsonify({'message': 'User not found!'}) 

if __name__ == '__main__': 
	app.run(debug=True).

