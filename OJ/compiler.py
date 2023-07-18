
import subprocess
import os

def compile_code(file_path, language):
    import shutil
    if language == 'c':
        compiler = 'gcc'
    elif language == 'cpp':
        compiler = 'g++'
    elif language == 'py':
        return
    else:
        return
    try:
        subprocess.run([compiler, file_path],capture_output=True)
        source_file = "/home/ayush/Documents/AlgoUni_Project/OJ/a.out"
        destination_file = "/home/ayush/Documents/AlgoUni_Project/OJ/OJ/waste"
        shutil.move(source_file, destination_file)
        subprocess.run(['rm',file_path])
        executable_file_path = destination_file
        print("Code compiled successfully.")
        return executable_file_path
    except:
        print("Error occurred while compiling the code.")

def run_code(compiled_file_path,language,input):

    if language == 'c':
        executable = './a.out'
    elif language == 'cpp':
        executable = './a.out'
    elif language == 'py':
        executable = 'python'
    else:
        return
    try:
        print(compiled_file_path)
        print(executable)
        os.chdir("OJ/waste")
        result = subprocess.run([f"{executable}"],input=input.encode(),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        subprocess.run(['rm',"a.out"])
        os.chdir("../../")
        stdout_output = result.stdout.decode()
        stderr_output = result.stderr.decode()
        if stderr_output:
            answer = stderr_output
            return answer
        else:
            answer = stdout_output
            print("code executed successfully")
            return answer
        return answer

    except:
        print("Error occurred while executing the code.")





