a = 1
i = 0
for i in range(0,10):
    a = get("user")
    a = clean(a)
    a = mogrify(a)
send_mail_jinja(a)
execute(b)
