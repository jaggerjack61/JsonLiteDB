
import json

import Rules as rule

class Database:
	def __init__(self, filename):
		self.filename = filename

	def create_table(self, table_name, schema):
		with open(self.filename, 'r+',encoding='utf-8') as json_file:
			database = json.load(json_file)
			if table_name in database:
				print('Table already exists!')
			else:
				database[table_name] = {}
				database[table_name]['schema']=schema
				json_file.seek(0)
				json.dump(database, json_file, indent=4)

	def insert_data(self, table_name, data):
		with open(self.filename, 'r+', encoding='utf-8') as json_file:
			database = json.load(json_file)
			ru = rule.Rules()
			
			if table_name in database:
				if 'values' in database[table_name]:
					if(ru.validate(data,database[table_name]['schema'])):
						table = database[table_name]['values']
						table.append(data)
						database[table_name]['values'] = table
						json_file.seek(0)
						json.dump(database, json_file, indent=4)
				else:
					database[table_name]['values'] = []
					if(ru.validate(data,database[table_name]['schema'])):
						table = database[table_name]['values']
						table.append(data)
						database[table_name]['values'] = table
						json_file.seek(0)
						json.dump(database, json_file, indent=4)
			else:
				print('Table does not exist!')

	def delete_data(self, table_name, data):
		with open(self.filename, 'r+', encoding='utf-8') as json_file:
			database = json.load(json_file)
			if table_name in database:
				table = database[table_name]['values']
				for item in table:
					if item == data:
						table.remove(item)
						database[table_name]['values'] = table
						json_file.seek(0)
						json.dump(database, json_file, indent=4)
						print('Data deleted successfully!')
					
			else:
                                print('Table does not exist!')
                                
	def search_data(self, table_name, search_data):
			with open(self.filename, 'r') as json_file:
				database = json.load(json_file)
				if table_name in database:
						table = database[table_name]['values']
						for item in table:
								print('here')
								if item == search_data:
										print('Data found!')
						print('Data not found!')
				else:
					print('Table does not exist!')

	
	# def create_database(self, database_name):
    # 	with open(self.filename, 'r+') as json_file:
    #         database = json.load(json_file)
    #         if database_name in database:
    #             print('Database already exists!')
    #         else:
    #             database[database_name] = []
    #             json_file.seek(0)
    #             json.dump(database, json_file, indent=4)
    #             print('Created')

#db = Database('databse.json')
