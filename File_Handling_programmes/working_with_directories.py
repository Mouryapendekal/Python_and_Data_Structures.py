import os
# 1. Get current working directory
directory = os.getcwd()
print("Current directory:", directory)
# 2. List all entries
all_files = os.listdir(directory)
print("\nAll entries:", all_files)
# 3. Filter text files
txt_files = [
    file for file in all_files
    if file.endswith(".txt")
]
print("\nText files:", txt_files)
# 4. Read and store contents of each text file
all_data = {}
for file in txt_files:
    with open(os.path.join(directory, file),
              "r", encoding="utf-8") as f:
        all_data[file] = f.read()
# 5. Display contents of each file
for filename, data in all_data.items():
    print(f"\nContents of {filename}:")
    print(data)
