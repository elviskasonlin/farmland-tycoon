"""
config_json_rw.py

To test whether json rw works.
Note: This is not an actual test implementation
"""

import json

# Read file
r_filename = "./config/default_crops.json"

f = open(r_filename, "r")
data_as_dict = json.load(f)
f.close()

print(data_as_dict)
print(len(data_as_dict))

for each in data_as_dict.items():
    print(each[0])
    print(each[1]["time"])

# Save file
w_filename = "./tests/config_json_rw.json"

f = open(w_filename, "w")
json.dump(data_as_dict, f)
f.close()