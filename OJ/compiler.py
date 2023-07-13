
import subprocess
import os

def extension_adder(language,file):
    if language == 'C':
        return file+'.c'
    elif language == 'C++':
        return file+'.cpp'
    elif language == 'Python':
        return file+'.py'
    else:
        return file+'.txt'


def save_text_file(file_path,code):
    code = subprocess.run(['echo', code],capture_output=True)
    with open(file_path, 'w') as f:
        f.write(code.stdout.decode('utf-8'))
    print("Text file saved successfully.")

import os

def change_file_extension(file_path, language):
    if language == 'C':
        new_extension = '.c'
    elif language == 'C++':
        new_extension = '.cpp'
    elif language == 'Python':
        new_extension = '.py'
    else:
        new_extension = '.txt'
    file_name, _ = os.path.splitext(file_path)
    new_file_path = file_name + new_extension
    try:
        os.rename(file_path, new_file_path)
        print("File extension changed successfully.")
    except OSError as e:
        print(f"An error occurred: {e}")

def change_file_name(file_path, new_name):
    try:
        dir_name = os.path.dirname(file_path)
        new_file_path = os.path.join(dir_name, new_name)
        os.rename(file_path, new_file_path)
        print("File name changed successfully.")
    except OSError as e:
        print(f"An error occurred: {e}")







