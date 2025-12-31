import pandas as pd
from docx.shared import Mm
from docxtpl import DocxTemplate, InlineImage


def create_docx():
    pass

def pdf_output():
    pass

doc = DocxTemplate('tepmlate.docx')

context = {
    "event_name": ,
    "unit_name": ,
    "event_date": ,
    "event_locaition": ,
    "schedule": ,

}

doc.render(context)
doc.save("output.docx")