username = get('username')
query = 'SELECT * from User WHERE username = \'' + username + '\';'
user_info = execute(query)
