import json
from jsonpath_ng import parse
from robot.api.deco import keyword


class JsonUtils:

    # Refer to: https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#dynamic-library-api
    def get_keyword_names(self):
        attributes = [(name, getattr(self, name)) for name in dir(self)]
        keywords = [(name, value) for name, value in attributes if hasattr(value, 'robot_name')]
        return [value.robot_name or name for name, value in keywords]

    def load_json(self, json_string):
        try:
            return json.loads(json_string)
        except Exception as e:
            raise ValueError(f"Invalid JSON: {json_string}")

    def is_valid_jsonpath(self, json_path):
        try:
            parse(json_path)
            return True
        except Exception as e:
            return False

    @keyword
    def get_json_values(self, json_data, json_path):
        if not self.is_valid_jsonpath(json_path):
            raise ValueError(f"Invalid JSON path: {json_path}")
        jsonpath_expr = parse(json_path)
        matches = jsonpath_expr.find(self.load_json(json_data))
        if matches:
            return [match.value for match in matches]
        else:
            return None

    @keyword
    def get_json_value(self, json_data, json_path):
        values = self.get_json_values(json_data, json_path)
        return values[0] if values else None
