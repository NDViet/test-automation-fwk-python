from ndviet_test_automation.utilities.src.test_object.test_object import TestObject
from ndviet_test_automation.utilities.src.test_object.web_test_object import WebTestObject


class ObjectRepository:
    @staticmethod
    def find_test_object(relative_object_id, variables=None):
        if variables is None:
            variables = {}
        try:
            to = WebTestObject(relative_object_id, variables)
        except Exception as e:
            raise RuntimeError(
                f"Could not find test object with ID: '{relative_object_id}'. Kindly check the relativeObjectId is "
                f"correct!")
        return to
