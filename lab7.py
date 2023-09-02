import os  
import zipfile  
def backup_folder_to_zip(source_folder, zip_filename):  
  if not os.path.exists(source_folder):  
    print (f"Error: Source folder '{source_folder}' does not exist.") 
    return  
  zipf = zipfile.ZipFile(zip_filename, 'w')  
  for foldername, subfolders, filenames in os.walk (source_folder):  
    for filename in filenames:  
     file_path = os.path.join(foldername, filename)  
     zipf.write(file_path, os.path.relpath(file_path, source_folder))  
     print(f"Zipping: {file_path}")  
   zipf.close()  
   print(f"Backup successful: '{source_folder}' has been backed up to '{zip_filename}.") 
folder_to_backup= input("Enter the name of the folder to backup : ") 
zip_filename = f"{folder_to_backup}.zip" 
backup_folder_to_zip(backup_folder_to_zip,zip_filename)
