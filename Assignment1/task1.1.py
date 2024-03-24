import json
import threading

def parse_json_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
        print(f"Contents of {file_name}:")
        print(json.dumps(data, indent=4))
        print()

def create_json_file(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file)

data1 = {"name": "John", "age": 30, "city": "New York"}
data2 = {"name": "Alice", "age": 25, "city": "Los Angeles"}

create_json_file("file1.json", data1)
create_json_file("file2.json", data2)

file_names = ["file1.json", "file2.json"]

threads = []
for file_name in file_names:
    thread = threading.Thread(target=parse_json_file, args=(file_name,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

