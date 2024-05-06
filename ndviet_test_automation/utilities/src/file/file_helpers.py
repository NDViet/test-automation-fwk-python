import os


class FileHelpers:
    @staticmethod
    def get_path(path):
        if path is not None:
            return os.path.abspath(path)
        else:
            return path

    @staticmethod
    def get_file_name(path):
        file_path = FileHelpers.get_path(path)
        return os.path.basename(file_path)

    @staticmethod
    def is_directory(path, create_if_not_exist=True):
        if not os.path.exists(path) and create_if_not_exist:
            os.makedirs(path)
        return os.path.isdir(path)

    @staticmethod
    def recursive_get_list_files(directory, all_files=None, filter_file_type=None):
        if all_files is None:
            all_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if filter_file_type is None or file.endswith(filter_file_type):
                    all_files.append(os.path.join(root, file))
        return all_files
