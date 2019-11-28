username = get('username')
head = '<head><title>%s profile</title></head>' % username
response = make_response(head)
