import collections


class DictUtils:
    @staticmethod
    def get_segments(segments_path):
        return segments_path.split(".")

    @staticmethod
    def get_value_as_string(dict, segments_path):
        segments = DictUtils.get_segments(segments_path)
        value = DictUtils.get_nested_dict_value(dict, segments)
        if value is not None:
            return str(value)
        return None

    @staticmethod
    def get_value_as_object(dict, segments_path):
        segments = DictUtils.get_segments(segments_path)
        value = DictUtils.get_nested_dict_value(dict, segments)
        return value

    @staticmethod
    def get_nested_dict_value(nested_dict, keys):
        if keys and isinstance(nested_dict, dict):
            key = keys[0]
            remaining_keys = keys[1:]
            if key in nested_dict:
                if remaining_keys:  # If there are more keys, recurse
                    return DictUtils.get_nested_dict_value(nested_dict[key], remaining_keys)
                else:  # If no more keys, return the value
                    return nested_dict[key]
        return None  # Return None if keys list is empty or nested_dict is not a dictionary

    @staticmethod
    def recursive_merge(dict1, dict2):
        for key in dict2:
            if key in dict1 and isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                DictUtils.recursive_merge(dict1[key], dict2[key])
            else:
                dict1[key] = dict2[key]

    @staticmethod
    def sort_by_keys(dict, reverse=False):
        return dict(sorted(dict.items(), key=lambda item: item[0], reverse=reverse))

    @staticmethod
    def sort_by_values(dict, reverse=False):
        return dict(sorted(dict.items(), key=lambda item: item[1], reverse=reverse))
