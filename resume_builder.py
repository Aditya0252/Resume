from jinja2 import Environment, FileSystemLoader
from docx import Document

def build_resume(data: dict, option: int):
    env = Environment(loader=FileSystemLoader("templates"))
    template_file = f"resume_{option}.jinja"
    template = env.get_template(template_file)

    rendered = template.render(data)
    doc = Document()
    doc.add_paragraph(rendered)
    path = f"data/resume_{data['name'].replace(' ', '_')}.docx"
    doc.save(path)
    return path
