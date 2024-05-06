from ndviet_test_automation.utilities.src.template.template_heplers import TemplateHelpers
from ndviet_test_automation.utilities.src.test_object.test_object import TestObject
from ndviet_test_automation.utilities.src.test_object.web_element_identifier import WebElementIdentifier


class WebTestObject(TestObject):
    def __init__(self, relative_object_id, variables):
        super().__init__(relative_object_id, None)
        self.relative_object_id = relative_object_id
        self.value = WebElementIdentifier.get_instance().get_identifier(relative_object_id)
        print(f"Object ID: {self.relative_object_id} - Object value: {self.value}")
        self.value = TemplateHelpers.process_template(self.value, variables)
