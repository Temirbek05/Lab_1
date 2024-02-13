import json

with open('sample-data.json') as file:
    json_data = json.load(file)

print("Interface Status")
print("=" * 80)
print("{:<50}{:<25}{:<8}{:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

iamdata = json_data["imdata"]

for item in iamdata:
    nt_item = item["l1PhysIf"]
    att = nt_item["attributes"]
    dn = att["dn"]
    description = att.get("descr", "")
    speed = att.get("speed", "inherit")
    mtu = att.get("mtu", "")
    
    print("{:<50}{:<25}{:<8}{:<6}".format(dn, description, speed, mtu))

