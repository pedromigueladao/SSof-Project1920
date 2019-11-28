username = get('username')
username = escape_string(username)
query = 'SELECT * from User WHERE username=\'%s\' AND password=\'%s\';' % (username, password)
user_info = execute(query)
