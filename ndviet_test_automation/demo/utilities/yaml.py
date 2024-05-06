import yaml
from robot.api.deco import keyword
from ndviet_test_automation.demo.utilities.files import FileUtils


class YamlUtils:
    @keyword('convertYamlToDictionary')
    def load_yaml(self, yaml_string):
        try:
            return yaml.safe_load(yaml_string)
        except Exception as e:
            raise ValueError(f"Invalid YAML: {yaml_string}")

    def load_yaml_file(self, file_path):
        try:
            file_path = FileUtils.normalize_path(file_path)
            with open(file_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{file_path}' not found.")
        except Exception as e:
            raise ValueError(f"An error occurred: {e}")

    @keyword
    def get_yaml_value(self, file_path, key_path):
        try:
            file_path = FileUtils.normalize_path(file_path)
            yaml_data = self.load_yaml_file(file_path)
            value = self._traverse_yaml(yaml_data, key_path.split('.'))
            return value
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def _traverse_yaml(self, yaml_data, key_path):
        for key in key_path:
            yaml_data = yaml_data.get(key)
            if yaml_data is None:
                raise KeyError(f"Key '{key}' not found.")
        return yaml_data

    @keyword
    def edit_yaml_key(self, yaml_data, key_path, new_value, output_file_path=None):
        try:
            # Update key value
            keys = key_path.split('.')
            current = yaml_data
            for key in keys[:-1]:
                current = current[key]
            current[keys[-1]] = new_value
            print(f"Key '{key_path}' updated successfully with value '{new_value}'.")

            if output_file_path:
                output_file_path = FileUtils.normalize_path(output_file_path)
                return self.write_yaml_file(output_file_path, yaml_data)
            else:
                print("Changes returned as YAML string.")
                return yaml.dump(yaml_data)
        except Exception as e:
            print(f"An error occurred: {e}")

    @keyword(name='createYamlFile')
    def write_yaml_to_file(self, yaml_data, file_path):
        try:
            yaml_data = self.load_yaml(yaml_data)
            file_path = FileUtils.normalize_path(file_path)
            with open(file_path, 'w') as file:
                yaml.dump(yaml_data, file)
            print(f"YAML data saved to '{file_path}'.")
            return file_path
        except Exception as e:
            print(f"An error occurred: {e}")
