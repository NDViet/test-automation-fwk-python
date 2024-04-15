import os


class FileUtils:
    @staticmethod
    def normalize_path(path):
        if not os.path.isabs(path):
            path = os.path.join(os.getcwd(), path)
        return os.path.normpath(path)
