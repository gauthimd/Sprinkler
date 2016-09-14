import json
with open('status.json') as infile:
 data = json.load(infile)
infile.close()
print data
print data["control"]
print type(data["control"])
print data["pump"]
print type(data["pump"])
print data["zone"]
print type(data["zone"])
newdata = {"control": "Auto", "pump": True, "zone": [[1,20],[2,15]]}
with open('status.json','w') as outfile:
 json.dump(newdata, outfile, indent=4)
outfile.close()
with open('status.json') as infile:
 again = json.load(infile)
infile.close()
print again
print again["control"]
again["control"] = str(again["control"])
print type(again["control"])
print again["pump"]
print type(again["pump"])
print again["zone"]
print type(again["zone"])
for x in again["zone"]:
 y = x
 r = y[0]
 s = y[1]
 print y, r, s, type(y), type(r), type(s)
if again["control"] == "Auto":
 print "True"
else: print "False"
if type(y) == list: print "Double True"
