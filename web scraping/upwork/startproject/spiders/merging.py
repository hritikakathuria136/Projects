import json
import glob

# create an empty list to store all the data
data_list = []


for i in range(1, 6):
    with open(f"/Users/hritikakathuria/upwork/startproject/data{i}.json", "r", encoding="utf-8") as f:
        # read the entire contents of the file as a string
        file_contents = f.read()
        # parse the string as JSON and append each dictionary to the data_list
        data_list.extend(json.loads(file_contents))


# write the combined data to a new file
with open("combined_data.json", "w", encoding="utf-8") as f:
    json.dump(data_list, f)
