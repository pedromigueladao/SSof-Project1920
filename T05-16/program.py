nis=get('nis')
query=""
arg1=""
arg2=""
arg3=""
while nis == "":
      query = query + arg3
      arg3 = arg2
      arg2 = arg1
      arg1 = nis
      query = escape_string(query,1)
q=execute(query)


