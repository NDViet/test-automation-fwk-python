import os
import tempfile
from jinja2 import Environment, FileSystemLoader, select_autoescape


class TemplateHelpers:
    m_instance = None
    m_templates_directory = None

    def __init__(self, templates_directory=None):
        self.env = Environment(
            loader=FileSystemLoader(templates_directory or '/'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        TemplateHelpers.m_templates_directory = templates_directory

    @staticmethod
    def get_instance():
        if TemplateHelpers.m_instance is None:
            TemplateHelpers.m_instance = TemplateHelpers()
        return TemplateHelpers.m_instance

    @staticmethod
    def process_template(template_string, variables):
        if variables is None:
            return template_string
        template = TemplateHelpers.get_instance().env.from_string(template_string)
        return template.render(variables)

    @staticmethod
    def process_file_template(source_path, variables, target_path=None):
        source_path = os.path.abspath(source_path)
        template_name = os.path.basename(source_path)
        template_directory = os.path.dirname(source_path)
        TemplateHelpers(template_directory)
        template = TemplateHelpers.get_instance().env.get_template(template_name)
        if target_path is None:
            temp_file = tempfile.NamedTemporaryFile(dir=os.getcwd(), delete=False)
            target_path = temp_file.name
        with open(target_path, 'w') as f:
            f.write(template.render(variables))
        return target_path
