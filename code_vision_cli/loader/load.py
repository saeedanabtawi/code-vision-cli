import os

from tqdm import tqdm


def load_code_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except IOError as e:
        print('[-] Error : ' + str(e))
        return


def load_code_from_dir(dir_path):
    # @TODO handle if folder is not readable
    # @TODO read only c files
    code_files = os.listdir(dir_path)

    code_dict = {}
    for code_file in tqdm(code_files, desc="[+] Loading code files", unit='file'):
        code_path = os.path.join(dir_path, code_file)
        # Additional handling for different file extensions can be added here
        code_file_key = code_file.replace('.cpp', '')
        code_dict[code_file_key] = load_code_from_file(code_path)

    return code_dict
