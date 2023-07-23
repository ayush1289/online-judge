import subprocess
import os


def compile_code(file_path, lang):
    if lang == "c":
        compiler = "gcc"
    elif lang == "cpp":
        compiler = "g++"
    else:
        return

    curr_dir = os.getcwd()
    try:
        os.chdir("OJ/waste")
        compile_file = subprocess.run([compiler, file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        os.chdir(curr_dir)
        stderror = compile_file.stderr.decode("utf-8")
        if stderror == "":
            return  "Compilation successful"
        else:
            return "Compilation Error"
    except:
        os.chdir(curr_dir)
        return "Compilation Error"


def run_code(lang, ip_data):
    curr_dir = os.getcwd()
    try:
        os.chdir("OJ/waste")

        if lang == "py":
            result = subprocess.run(
                ["python", "temp.py"],
                input=ip_data.encode(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=5,
            )
        else:
            result = subprocess.run(
                ["./a.out"],
                input=ip_data.encode(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=5,
            )
        os.chdir(curr_dir)
        stdout_output = result.stdout
        stderr_output = result.stderr

        if result.returncode != 0:
            raise subprocess.CalledProcessError(
                result.returncode,
                cmd=result.args,
                output=result.stdout,
                stderr=result.stderr,
            )
        return result.stdout.decode("utf-8")

    except FileNotFoundError as e:
        os.chdir(curr_dir)
        print(f"Error: {e.filename} not found.")
        return "Error: File not found."
    except PermissionError as e:
        os.chdir(curr_dir)
        print(f"Error: Permission denied for {e.filename}.")
        return "Error: Permission denied."
    except subprocess.CalledProcessError as e:
        os.chdir(curr_dir)
        print(f"Error: Command {e.cmd} returned a non-zero exit code {e.returncode}.")
        print(f"Standard Output: {e.output}")
        print(f"Standard Error: {e.stderr}")
        return "Error: Code execution failed."
    except subprocess.TimeoutExpired as e:
        os.chdir(curr_dir)
        print(f"Error: Code execution timed out. {e}")
        return "Time Limit Exceeded."
    except Exception as e:
        os.chdir(curr_dir)
        print(f"Error occurred while executing the code: {e}")
        return "Error occurred while executing the code."


def check_tc(tc, language):
    flag = 1
    j = 0
    idx = 0
    for i in tc:
        j += 1
        result = run_code(language, str(i.tc_input).replace(" ", "\n"))
        result = result.replace("\n", "").replace(" ", "")

        if result != i.tc_output:
            flag = 0
            idx = j
            break
    if flag == 0:
        return f"Wrong Answer on tc {idx}"
    else:
        return "Accepted"
