from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086)

print(client.get_list_database())

## Returns: [{'name': 'telegraf'}, {'name': '_internal'}]

client.switch_database('telegraf')

print(client.query('SELECT * FROM "telegraf"."autogen"."processes"'))