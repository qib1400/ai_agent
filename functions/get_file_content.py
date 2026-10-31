from config import max_chars
import os


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        target_path = os.path.join(abs_path, file_path)
        norm_target_path = os.path.normpath(target_path)
        valid_target_path = os.path.commonpath([abs_path, norm_target_path]) == abs_path

        if not valid_target_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if os.path.isfile(norm_target_path):
            with open(norm_target_path, 'r') as f:
                content = f.read(max_chars)
                if f.read(1):
                    content += f'[...File "{file_path}" truncated at {max_chars} characters]'
                return content
        else:
            return f'Error: File not found or is not a regular file: "{file_path}"'
    except Exception as e:
        return f'Error: {e}'