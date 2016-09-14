d = {5,6,13,19,26,12,16,20}
for x in d: print x
l = [5,6,13,19,26,12,16,20]
for x in l: print x
if all(isinstance(x, int) for x in l): print "Ringadingdingmuthafucka"
li = [[22,4],[13,5],[20,3]]
if all(isinstance(x, list) for x in li): print "Yippykyaymuthafucka"
