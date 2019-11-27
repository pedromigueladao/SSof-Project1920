id = get('id')
user = 'admin' if not id else 'guest'
query = 'SELECT * FROM user WHERE username=\'%s\'' % user
row = execute(query)
