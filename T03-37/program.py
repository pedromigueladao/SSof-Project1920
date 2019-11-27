uname = 17
uname = copy()
q = mark_safe(uname, copy())

q = mark_safe(uname, ContactMailForm(clean(get_object_or_404())))
