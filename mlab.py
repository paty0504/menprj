import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds147469.mlab.com:47469/who-2-call
# mongodb://<dbuser>:<dbpassword>@ds119490.mlab.com:19490/menprj

host = "ds119490.mlab.com"
port = 19490
db_name = "menprj"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
