import json

import Rules as rule


class Database:
    def __init__(self, filename):
        self.filename = 'databases/'+filename
        self.ru = rule.Rules()

    def create_table(self, table_name, schema):
        schema = self.ru.check_id_schema(schema)
        with open(self.filename, 'r+', encoding='utf-8') as json_file:
            database = json.load(json_file)
            if table_name in database:
                print('Table already exists!')
            else:
                database[table_name] = {}
                database[table_name]['schema'] = schema
                database[table_name]['values'] = []
                json_file.seek(0)
                json.dump(database, json_file, indent=4)

    def insert_data(self, table_name, data):
        with open(self.filename, 'r+', encoding='utf-8') as json_file:
            database = json.load(json_file)
            data = self.ru.check_id_values(database, table_name, data)
            if table_name in database:
                if 'values' in database[table_name]:
                    if self.ru.validate(data, database[table_name]['schema']):
                        table = database[table_name]['values']
                        table.append(data)
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
    def getRecords(self, table):
        output = {}
        with open(self.filename, 'r') as json_file:
            database = json.load(json_file)
            for table_name, table_data in database.items():
                # Get the schema and values of the table
                schema = table_data["schema"]
                values = table_data["values"]
                # Create an empty list to store the rows of the table
                if(table_name == table):
                    output[table_name] = []
                    # Loop through each row in values
                    for row in values:
                        # Create an empty dictionary to store the columns of the row
                        output_row = {}
                        # Loop through each column in schema
                        for column in schema:
                            # Get the name and type of the column
                            name = column["name"]
                            type = column["type"]
                            # Get the value of the column for this row
                            value = row[name]
                            # Convert the value to its type if needed
                            if type == "integer":
                                value = int(value)
                            elif type == "float":
                                value = float(value)
                            # Store the value with its name in the output row dictionary
                            output_row[name] = value
                        # Append the output row dictionary to the output table list
                        output[table_name].append(output_row)

                # Return the output dictionary as well (optional)
            print(output)
            return output


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

# db = Database('databse.json')
