id = get('id')
if id == 0:
    user = 'admin'
else:
    user = 'guest'
info = get_user_password(user)
