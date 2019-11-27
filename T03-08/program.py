name =  request.form.get()
q = cursor.execute("SELECT pass FROM users WHERE user='%s'" % name)