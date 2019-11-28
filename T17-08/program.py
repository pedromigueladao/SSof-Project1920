user = get('user')
user_id = escape_string(user)
valid_user = user if user_id != 'admin' else 'guest'
get_user_password(valid_user)
