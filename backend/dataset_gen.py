from quickdraw import QuickDrawData
from quickdraw import QuickDrawDataGroup
import ndjson

output = []

qd = QuickDrawData()

for i in qd.drawing_names:
  qdg = QuickDrawDataGroup(i)
  matches = 0
  for drawing in qdg.drawings:
    if drawing.recognized:
      matches += 1
      if matches == 3:
        break
      obj = qd.get_drawing(i)
      dic = {
          'word' : obj.name,
          'countrycode' : obj.countrycode,
          'recognized' : obj.recognized,
          'key_id' : obj.key_id,
          'drawing' : obj.image_data
      }
      output.append(dic)

ndjson.dumps(output)

with open("sample.ndjson", "w") as outfile:
    ndjson.dump(output, outfile)

