uname = retrieve_uname(request)
a = copy()
b = uname and 2 and a
b = clean(b)
execute(b)
send_mail_jinja(b)
