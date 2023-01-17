
import json 

class Database: 
	def __init__(self, filename): 
		self.filename = filename 

	def create_table(self, table_name, schema): 
		with open(self.filename, 'r+') as json_file: 
			database = json.load(json_file)
			if table_name in database: 
				print('Table already exists!') 
			else: 
				database[table_name] = schema 
				json_file.seek(0) 
				json.dump(database, json_file, indent=4) 

	def insert_data(self, table_name, data): 
		with open(self.filename, 'r+') as json_file: 
			database = json.load(json_file) 
			if table_name in database: 
				table = database[table_name] 
				table.append(data) 
				database[table_name] = table 
				json_file.seek(0) 
				json.dump(database, json_file, indent=4) 
			else: 
				print('Table does not exist!') 

	def delete_data(self, table_name, data): 
		with open(self.filename, 'r+') as json_file: 
			database = json.load(json_file) 
			if table_name in database: 
				table = database[table_name] 
				for item in table: 
					if item == data: 
						table.remove(item) 
						database[table_name] = table 
						json_file.seek(0) 
						json.dump(database, json_file, indent=4) 
                        print('Data deleted successfully!') 
            else: 
                print('Table does not exist!')

    def search_data(self, table_name, search_data): 
		with open(self.filename, 'r') as json_file: 
			database = json.load(json_file) 
			if table_name in database: 
				table = database[table_name] 
				for item in table: 
					if item == search_data: 
						return 'Data found!'
				return 'Data not found!'
			else: 
				print('Table does not exist!')

    def create_database(self, database_name): 
        with open(self.filename, 'r+') as json_file: 
            database = json.load(json_file) 
            if database_name in database: 
                print('Database already exists!') 
            else: 
                database[database_name] = []
                json_file.seek(0) 
                json.dump(database, json_file, indent=4)
                print('Created') 

