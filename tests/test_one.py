import json

# Read file
filename = "./config/default_crops.json"

f = open(filename, "r")
data_as_dict = json.load(f)
f.close()

print(data_as_dict)
print(len(data_as_dict))

for each in data_as_dict.items():
    print(each[0])
    print(each[1]["time"])

# Save file

f = open()