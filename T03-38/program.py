uname = ContactMailForm()
uname = ChatMessageForm(uname)
uname = "i am safe"
q = mark_safe("SELECT pass FROM users WHERE user='%s'" % uname)
