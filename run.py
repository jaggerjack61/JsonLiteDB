import Database as db

js = db.Database('newDB.json')
js.create_database()
js.create_table('users', [{'name': 'id', 'type': 'integer'},
                          {'name': 'name', 'type': 'string'},
                          {'name': 'email', 'type': 'string', 'encrypted': True}
                          ], )
js.create_table('bills', [{'name': 'patient_id', 'type': 'integer'}, {'name': 'amount', 'type': 'float'},
                          {'name': 'currency', 'type': 'string'}, {'name': 'year', 'type': 'integer'}])
js.insert_data('users', {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'})
# print(js.search_id('patients', 5))
# js.delete_id('patients',4)
# js.create_database('hospital')
# js.getSchema('patients')
js.get_records('users')
