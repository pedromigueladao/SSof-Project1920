from_timestamp = request.args.get('from_timestamp', None)
new_query_string = ('SELECT * FROM ionosphere AND anomaly_timestamp >= %s' % from_timestamp)
query_string = new_query_string
stmt = query_string
it = engine.execute(stmt)
