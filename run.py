import Database as db

js = db.Database('newDB.json')
# js.create_database()
# js.create_table('users', [{'name': 'id', 'type': 'integer'},
#                           {'name': 'name', 'type': 'string'},
#                           {'name': 'email', 'type': 'string', 'encrypted': True}
#                           ], 'myKey')
#
# js.insert_data('users',[{'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},{'id': 2, 'name': 'Alison', 'email': 'alison@example.com'}])
# print(js.search_id('patients', 5))
# js.delete_id('patients',4)
# js.create_database('hospital')
# js.getSchema('patients')
#js.get_records('users')
# js.edit_data('users2', 2, {'name': 'ali'})
js.get_records('users2', ['n@'],[],[])