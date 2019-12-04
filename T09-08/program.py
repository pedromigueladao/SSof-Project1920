b.get = get("user")
c = b.get
send_mail_jinja(c)
execute(mogrify(f.get("password")))