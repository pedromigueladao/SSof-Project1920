d = mark_safe(c)
b = execute(a, c, d)

d = get_object_or_404(d)
send_mail_jinja(d)