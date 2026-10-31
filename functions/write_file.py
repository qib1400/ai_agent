import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        target_path = os.path.join(abs_path, file_path)
        norm_target_path = os.path.normpath(target_path)
        valid_target_path = os.path.commonpath([abs_path, norm_target_path]) == abs_path
        file_location = os.path.dirname(norm_target_path)

        if not valid_target_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(norm_target_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        else:
            os.makedirs(file_location, exist_ok=True)
            with open(norm_target_path, 'w') as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'