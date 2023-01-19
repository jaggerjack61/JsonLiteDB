import json

class Rules:

    def validate(self,data,schema):
        print(data,schema)
        parsed_data = json.dumps(data)
        print(parsed_data)
        for key in data:
            i=0
            for column in schema:
                if(column['name']==key):
                    i=1
                    print("Key "+key+" specified in the schema")
            if not (i==1):   
                print("Key "+key+" is not specified in the schema")
                return False
                    
            # if any(key in d for d in schema):
            #     print("Key "+key+" specified in the schema")
                # return False
            # else:
            #     print("Key "+key+" is not specified in the schema")
            # if key not in schema:
            #     print("Key "+key+" is not specified in the schema")
            #     return False
            for i in range(len(schema)):
                key = schema[i]['name']
                dtype = schema[i]['type']
                if dtype == 'string':
                    if not isinstance(data[key], str):
                        print("Value "+data[key]+" does not match the type specified in the schema")
                        return False
                elif dtype == 'integer':
                    if not isinstance(data[key], int):
                        print("Value "+data[key]+" does not match the type specified in the schema")
                        return False
        return True