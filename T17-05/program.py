id = get('id')
real_id = -1
while real_id != id:
    real_id = real_id + 1
password = get_user_password_by_id(real_id)
