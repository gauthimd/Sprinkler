import json
with open('status.json') as infile:
 data = json.load(infile)
print data
print data["control"]
print type(data["control"])
print data["pump"]
print type(data["pump"])
print data["zone"]
print type(data["zone"])
newdata = {"control": "Auto", "pump": True, "zone": None}
with open('status.json','w') as outfile:
 json.dump(newdata, outfile)
with open('status.json') as infile:
 again = json.load(infile)
print again
print again["control"]
again["control"] = str(again["control"])
print type(again["control"])
print again["pump"]
print type(again["pump"])
