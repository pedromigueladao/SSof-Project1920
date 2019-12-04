user = request.form.get()
user = MySQLdb.escape_string(user)
q = cursor.execute("SELECT pass FROM users WHERE user='%s'" % user)
