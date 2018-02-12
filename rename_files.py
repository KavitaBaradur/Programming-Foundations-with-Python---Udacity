import os
def rename_files():
    #get file names
    file_list = os.listdir("/Users/kavitabaradur/Downloads/prank")
    print(file_list)
    saved_path = os.getcwd()
    print(saved_path)
    os.chdir("/Users/kavitabaradur/Downloads/prank")

    for file_name in file_list:
        print("The oldname "+filename)
        print("The new name "+file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_files()
              
