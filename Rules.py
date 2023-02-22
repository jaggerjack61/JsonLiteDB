import json


class Rules:

    def validate(self, data, schema):
        print(data, schema)
        parsed_data = json.dumps(data)
        print(parsed_data)
        for key in data:
            i = 0
            for column in schema:
                if column['name'] == key:
                    i = 1
            if not (i == 1):
                return False
            for i in range(len(schema)):
                key = schema[i]['name']
                dtype = schema[i]['type']
                if dtype == 'string':
                    if not isinstance(data[key], str):
                        return False
                elif dtype == 'integer':
                    if not isinstance(data[key], int):
                        return False
                elif dtype == 'float':
                    if not isinstance(data[key], float):
                        return False
        return True

    def check_id_schema(self, schema):
        for column in schema:
            if column['name'] == 'id':
                return schema
        schema.append({'name': 'id', 'type': 'integer'})
        return schema

    def check_id_values(self, database, table_name, data):
        id = 0
        if 'id' in data.values():
            return data
        else:
            if 'values' in database[table_name]:
                id = len(database[table_name]['values'])
                if id == 0:
                    id = 1
                else:
                    id = database[table_name]['values'][id - 1]['id'] + 1
            else:
                id = 1
            data.update({'id': id})
            return data
