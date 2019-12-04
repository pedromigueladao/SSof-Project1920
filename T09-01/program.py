a = get('user')
b = c
a = clean(a)
execute(a)
a = mogrify(a)
execute(a)
c = send_mail_jinja(b)
