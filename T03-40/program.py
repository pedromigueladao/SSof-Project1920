request
uname = get_query_string()
q = mogrify("SELECT pass FROM users WHERE user='%s'" % uname)
