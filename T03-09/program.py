name =  request.form.get()
name = "Ola"
q = cursor.execute("SELECT pass FROM users WHERE user='%s'" % name)
