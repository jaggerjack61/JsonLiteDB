import Database as db

js = db.Database('newDB.json')
#js.create_database()
#js.create_table('users', [{'name': 'id', 'type': 'integer'},
                          # {'name': 'name', 'type': 'string', 'length': 10},
                          # {'name': 'age', 'type': 'integer', 'length': 2},
                          # {'name': 'email', 'type': 'string', 'encrypted': True}
                          # ], 'myKey')
#
js.insert_data('me', { 'name': 'ali', 'age': 15, 'money': 5.0})#,{'id': 2, 'age': 5, 'name': 'Alison', 'email': 'alison@example.com'}])
# print(js.search_id('patients', 5))
# js.delete_id('patients',4)
# js.create_database('hospital')
# js.getSchema('patients')
#js.get_records('users')
# js.edit_data('users2', 2, {'name': 'ali'})
js.get_records('me')