from pathlib import Path
import shutil

data_folder = Path(__file__).parent / "data"

#files_in_folder = [file.name for file in data_folder.iterdir()]
#print(files_in_folder)

converted_files = list()

for file in data_folder.iterdir():
    if "txt" in file.suffix:
        converted_files.append(file.with_suffix(".csv"))

for file in converted_files:
    print(file)
        

