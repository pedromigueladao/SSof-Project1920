a = "I am not tainted"
while b:
    send_mail_jinja(a)
    a = ContactMailForm() + get_query_string()
execute(a)