import Database as db


js = db.Database('database.json')
js.create_table('patients',[ { 'name': 'name', 'type': 'string' }, { 'name': 'country', 'type': 'string' }, { 'name': 'category', 'type': 'string' }, { 'name': 'year', 'type': 'integer' } ])
js.search_data('patients', { 'name': 'sam', 'country':'zim', 'category':'ICU', 'year':2023 })
print(js.search_id('patients',5))
#js.create_database('hospital')