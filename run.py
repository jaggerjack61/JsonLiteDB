import Database as db

js = db.Database('database.json')
# js.create_table('patients', [{'name': 'name', 'type': 'string'}, {'name': 'country', 'type': 'string'},
#                              {'name': 'category', 'type': 'string'}, {'name': 'year', 'type': 'integer'}])
# js.create_table('bills', [{'name': 'patient_id', 'type': 'integer'}, {'name': 'amount', 'type': 'float'},
#                           {'name': 'currency', 'type': 'string'}, {'name': 'year', 'type': 'integer'}])
js.delete_data('patients', {'name': 'sam', 'country': 'zim', 'category': 'ICU', 'year': 2023,'id':2})
# print(js.search_id('patients', 5))
js.delete_id('patients',3)
# js.create_database('hospital')
