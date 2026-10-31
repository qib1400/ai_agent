import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        target_path = os.path.join(abs_path, file_path)
        norm_target_path = os.path.normpath(target_path)
        valid_target_path = os.path.commonpath([abs_path, norm_target_path]) == abs_path

        if not valid_target_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if os.path.isfile(norm_target_path):
            if not file_path.endswith(('.py')):
                return f'Error: "{file_path}" is not a Python file'
            else:
                command = ["python", norm_target_path]
                if args:
                    command.extend(args)
                completed_process = subprocess.run(command,cwd=working_directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=30)
                processed_output = []
                if completed_process.returncode != 0:
                    processed_output.append(f"Process exited with code {completed_process.returncode}")
                if not completed_process.stdout and not completed_process.stderr:
                    processed_output.append("No output produced")
                else:
                    if completed_process.stdout:
                        processed_output.append(f"STDOUT: {completed_process.stdout}")
                    if completed_process.stderr:
                        processed_output.append(f"STDERR: {completed_process.stderr}")
                return "\n".join(processed_output)
        else:
            return f'Error: "{file_path}" does not exist or is not a regular file'
    except Exception as e:
        return f"Error: executing Python file: {e}"