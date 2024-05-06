class TestObject:
    def __init__(self, relative_object_id, value):
        self.relative_object_id = relative_object_id
        self.value = value

    def get_value(self):
        return self.value

    def __str__(self):
        return f"Object ID: {self.relative_object_id} - Object value: {self.value}"
