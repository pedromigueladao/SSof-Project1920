user = get_query_string("user")
other_user = maybe_a_source()
if other_user == user:
    execute(other_user)
    escape_string(other_user)
else:
    raw(other_user)
RawSQL(other_user)