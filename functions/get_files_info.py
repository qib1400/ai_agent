import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
	try:
		abs_path = os.path.abspath(working_directory)
		target_path = os.path.join(abs_path, directory)
		norm_target_path = os.path.normpath(target_path)
		valid_target_path = os.path.commonpath([abs_path, norm_target_path]) == abs_path

		if not valid_target_path:
			return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

		if os.path.isdir(norm_target_path):
			dir_list = os.listdir(norm_target_path)
			file_info = []
			for file in dir_list:
				file_path = os.path.join(norm_target_path, file)
				is_dir = os.path.isdir(file_path)
				file_size = os.path.getsize(file_path)
				file_info.append(f"- {file}: file_size={file_size} bytes, is_dir={is_dir}")
			return "\n".join(file_info)
			# return f'Success: "{directory}" is within the working directory'
		else:
			return f'Error: "{directory}" is not a directory'
	except Exception as e:
		return f'Error: {e}'


