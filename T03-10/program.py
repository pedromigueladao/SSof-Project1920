name =  request.form.get()
name = MySQLdb.escape_string(name)
q = cursor.execute("SELECT pass FROM users WHERE user='%s'" % name)
