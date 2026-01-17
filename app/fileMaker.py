import pandas as pd
import streamlit as st
from docx.shared import Mm
from docxtpl import DocxTemplate, InlineImage
from TypeCast import *
from spire.doc import *
from spire.doc.common import *

def complite_print(form):
    docx_file = create_docx(form)
    document = Document()
    document.LoadFromFile(docx_file) 
    document.SaveToFile("event.pdf", FileFormat.PDF)
    document.Close()
    pdf_output("event.pdf")

def create_docx(form):
    time_comp = ""
    if (form.dates[2] == 1):
        time_comp = form.dates[0]
    else:
        time_comp = f"בין ה{form.dates[0]} ל{form.dates[1]}"

    doc = DocxTemplate("Template.docx")

    context = {
        "event_name": form.user[0] ,
        "unit_name": form.user[1] ,
        "event_date": time_comp ,
        "event_locaition": form.locaition ,
        "sum_ezrach": form.guests["azrach"] ,
        "sum_mil": form.guests["miloaim"] , #edit for casting int?
        "sum_keva": form.guests["keva"] ,
        "sum_sadir": form.guests["sadir"] ,
        "sum_all": form.guests["all"] ,
        "event_comander_name": form.personals[0][0],
        "event_comander_position": form.personals[0][1],
        "event_comander_phone": form.personals[0][2],
        "event_contact_name": form.personals[1][0],
        "event_contact_position": form.personals[1][1],
        "event_contact_phone": form.personals[1][2],
        #table for num2, + act.
        "schedule": form.schedule.to_dict(orient="records"),  
    }

    doc.render(context)
    doc.save("output.docx")

    return "output.docx" #docx_path #something?

def pdf_output(pdf_file):
    with open(pdf_file, "rb") as file:
        st.download_button("Download file", file, pdf_file)


