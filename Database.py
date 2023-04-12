import json
import secrets
import Rules as rule


class Database:
    def __init__(self, filename):
        self.filename = 'databases/'+filename
        self.ru = rule.Rules()

    def xor_encrypt(self, data, key):
        data_bytes = bytes(str(data), 'utf-8')
        key_bytes = bytes(key, 'utf-8')
        encrypted_bytes = bytes([data_byte ^ key_byte for (data_byte, key_byte) in zip(data_bytes, key_bytes * len(data_bytes))])
        return encrypted_bytes.hex()

    def xor_decrypt(self, data, key):
        data_bytes = bytes.fromhex(data)
        key_bytes = bytes(key, 'utf-8')
        decrypted_bytes = bytes([data_byte ^ key_byte for (data_byte, key_byte) in zip(data_bytes, key_bytes * len(data_bytes))])
        try:
            return int(decrypted_bytes.decode('utf-8'))
        except ValueError:
            try:
                return float(decrypted_bytes.decode('utf-8'))
            except ValueError:
                return decrypted_bytes.decode('utf-8')

    def create_table(self, table_name, schema, encryption_key=None):
        schema = self.ru.check_id_schema(schema)
        with open(self.filename, 'r+', encoding='utf-8') as json_file:
            database = json.load(json_file)
            if table_name in database:
                print('Table already exists!')
                return False
            else:
                database[table_name] = {}
                database[table_name]['schema'] = schema
                database[table_name]['values'] = []
                if encryption_key:
                    database[table_name]['encryption_key'] = encryption_key
                else:
                    encryption_key = secrets.token_hex(16)  # Generate a random 128-bit encryption key
                    database[table_name]['encryption_key'] = encryption_key
                json_file.seek(0)
                json.dump(database, json_file, indent=4)
                return True

    def insert_data(self, table_name, data):
        with open(self.filename, 'r+', encoding='utf-8') as json_file:
            database = json.load(json_file)
            data = self.ru.check_id_values(database, table_name, data)
            if table_name in database:
                if 'values' in database[table_name]:
                    if self.ru.validate(data, database[table_name]['schema']):
                        table = database[table_name]['values']

                        encrypted_data = {}
                        for key, value in data.items():
                            encryption_key = database[table_name].get('encryption_key')
                            for column in database[table_name]['schema']:
                                if column['name'] == key:
                                    if column.get('encrypted') and encryption_key:
                                        value = self.xor_encrypt(value, encryption_key)
                                    break
                            encrypted_data[key] = value

                        table.append(encrypted_data)
                        database[table_name]['values'] = table
                        json_file.seek(0)
                        json.dump(database, json_file, indent=4)
                else:
                    database[table_name]['values'] = []
                    if self.ru.validate(data, database[table_name]['schema']):
                        table = database[table_name]['values']
                        table.append(data)
                        database[table_name]['values'] = table
                        json_file.seek(0)
                        json.dump(database, json_file, indent=4)
            else:
                print('Table does not exist!')

    def get_records(self, table):
        output = {}
        with open(self.filename, 'r') as json_file:
            database = json.load(json_file)
            for table_name, table_data in database.items():
                if table_name == table:
                    schema = table_data["schema"]
                    values = table_data["values"]
                    encryption_key = table_data.get("encryption_key")
                    output[table_name] = []

                    for row in values:
                        output_row = {}
                        for column in schema:
                            name = column["name"]
                            type = column["type"]
                            encrypted = column.get("encrypted", False)
                            value = row[name]

                            if encrypted and encryption_key:
                                value = self.xor_decrypt(value, encryption_key)

                            if type == "integer":
                                value = int(value)
                            elif type == "float":
                                value = float(value)

                            output_row[name] = value
                        output[table_name].append(output_row)

            print(output)
            return output

    def delete_data(self, table_name, data):
        with open(self.filename, 'r+', encoding='utf-8') as json_file:
            database = json.load(json_file)
            if table_name in database:
                table = database[table_name]['values']
                for item in table:
                    if item == data:
                        table.remove(item)
                        database[table_name]['values'] = table
                        with open(self.filename, 'w+', encoding='utf-8') as json_file:
                            json_file.seek(0)
                            json.dump(database, json_file, indent=4)
                            print('Data deleted successfully!')

            else:
                print('Table does not exist!')

    def delete_id(self, table_name, id):
        with open(self.filename, 'r+', encoding='utf-8') as json_file:
            database = json.load(json_file)
            data = self.search_id(table_name, id)
            if data:
                if table_name in database:
                    table = database[table_name]['values']
                    for item in table:
                        if item == data:
                            table.remove(item)
                            database[table_name]['values'] = table
                            with open(self.filename, 'w+', encoding='utf-8') as json_file:
                                json_file.seek(0)
                                json.dump(database, json_file, indent=4)
                                print('Data deleted successfully!')

                else:
                    print('Table does not exist!')
            else:
                print('could not find specified record')

    def search_data(self, table_name, search_data):
        with open(self.filename, 'r') as json_file:
            database = json.load(json_file)
            if 'values' in database[table_name]:
                if table_name in database:
                    table = database[table_name]['values']
                    for item in table:
                        print('here')
                        if item == search_data:
                            print('Data found!')
                    print('Data not found!')
                else:
                    print('Table does not exist!')
            else:
                print('Table has no records')

    def search_id(self, table_name, id):
        with open(self.filename, 'r') as json_file:
            database = json.load(json_file)
            if 'values' in database[table_name]:
                if table_name in database:
                    table = database[table_name]['values']
                    for item in table:
                        if item['id'] == id:
                            return item
                            print('Data not found!')
                    return 'id does not exist'
                else:
                    return False
                    print('Table does not exist!')
            else:
                return False



    def getTables(self):
        output = []
        with open(self.filename, 'r') as json_file:
            database = json.load(json_file)
            for table_name, table_data in database.items():
                output.append({'name': table_name})

            print(output)
            return output


    def getDatabases(self):
        import os
        path = "databases"  # replace with your directory path
        json_files = [file for file in os.listdir(path) if file.endswith(".json")]  # get all files that end with .json
        data=[]
        for f in json_files:
            data.append({'name':f})
        print(data)
        return data  # print the list of json files

    def getSchema(self, table):
        output = {}
        with open(self.filename, 'r') as json_file:
            database = json.load(json_file)
            schema = None
            for table_name, table_data in database.items():
                # Get the schema and values of the table
                if table_name == table:
                    schema = table_data["schema"]
                    print(schema)
                    return schema



    def create_database(self):
        import os

        content = {}

        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump(content, f)
                print(f"Created {self.filename} with {content}")
                return True
        else:
            print(f"{self.filename} already exists")
            return False
# db = Database('databse.json')
