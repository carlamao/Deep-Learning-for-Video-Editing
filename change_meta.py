import json
import os

from pathlib import Path

data_folder = Path("/scratch-shared/ActiveNet/")
file_to_open = data_folder / "meta_all.json"
#filename = '/scratch-shared/ActiveNet/meta_all.json'

f =  open(file_to_open, 'r+')
data = json.load(f)
for i in data:
	print(data[i]['split'])

for i in datavi:
	if data[i]['split']== "anet_entities_cleaned_class_thresh50_trainval":
		data[i]['split'] = "train" # <--- add `id` value.
#os.remove(file_to_open)
with open(file_to_open, 'w') as file1:
    json.dump(data, file1)
file1.close()

import json
import os

from pathlib import Path

data_folder = Path("/scratch-shared/COOT/activitynet")
file_to_open = data_folder / "meta_all.json"
#filename = '/scratch-shared/ActiveNet/meta_all.json'

f =  open(file_to_open, 'r+')
data = json.load(f)
for i in data:
	print(data[i]['split'])