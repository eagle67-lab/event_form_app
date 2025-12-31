import streamlit as st
from streamlit_searchbox import st_searchbox
import pandas as pd
from functools import partial
from datetime import date,datetime,time,timedelta
from TypeCast import *
#import mymodel as m

def get_location():
    return None

def get_personals_data():
    col_a, col_b = st.columns(2)
    with col_a:
        event_comander_name = st.text_input("שם מפקד האירוע")
        event_comander_role = st.text_input("תפקיד המפקד")
        event_comander_phone = st.text_input("מפקד - מס' טלפון")
    with col_b:
        event_contact_name = st.text_input("שם איש הקשר")
        event_contact_role = st.text_input("תפקיד איש הקשר")
        event_contact_phone = st.text_input("איש קשר - מס' טלפון")

    return (event_comander_name,event_comander_role,event_comander_phone),(event_contact_name,event_contact_role,event_contact_phone)

def welcome():
    user = st.text_input("מה השם שלך?")
    st.write("ברוך הבא ", user)

    return st.checkbox("I agree to terms")
    #checkbox \ disclaimer

def get_dry_data():
    event_name = st.text_input("שם האירוע:")
    unit = st.text_input("שם היחידה:")
    start_date, end_date = st.date_input("תאריך האירוע:",value=(date.today(), date.today()),min_value=date(2000, 1, 1),max_value=date(9999, 12, 31))
    how_long = end_date - start_date 
    full_date = (start_date,end_date,how_long.days + 1)
    event_comander,event_contact = get_personals_data()
   
    return event_name,unit,full_date

def get_guest_count():
    st.subheader("כמות משתתפים באירוע:")

    col_a, col_b, col_c, col_d = st.columns(4)
    with col_a:
        sadir_num = st.number_input("חיילים בסדיר:",min_value=0, max_value=1000,step=1,value=0)
    with col_b:
        keva_num = st.number_input("חיילים בקבע:",min_value=0, max_value=1000,step=1,value=0)
    with col_c:
        azrach_num = st.number_input("אזרחים:",min_value=0, max_value=1000,step=1,value=0)
    with col_d:
        miloaim_num = st.number_input("חיילים במילואים:",min_value=0, max_value=1000,step=1,value=0)

    return {"sadir":sadir_num, "keva":keva_num,"azrach":azrach_num,"miloaim":miloaim_num,"all":sadir_num + keva_num + azrach_num + miloaim_num}

def create_supplier_list():


    return supplier_as_list

def create_activity_list(supplier_list):


    return relevant_activity_as_list

def get_price(chosen_activity,supplier):

    return [regular_price,full_price]

def rules():
    return recommend_status

def disclaimer():
    return check

def collect_activity():
    return None

def new_slot(df):
    #enter data
    new_row_data = {'Name': 'Charlie', 'Age': 35}
    new_row_df = pd.DataFrame([new_row_data]) # Must be in a list to create a DataFrame
    new_df = pd.concat([df, new_row_df], ignore_index=True)

    return new_df

def build_schedule():
    #node = [time_point,contents,place,remark]
    headers = ["שעה", "תוכנית", "מיקום", "הערה"]


    return full_schedule

def main():
    st.write("!ברוך הבא")
    check = welcome()
    if (check):
        my_form = Forms() 
        event_name,unit_name,event_date = get_dry_data()
        guest_count = get_guest_count()
        #event_schedule = build_schedule()
        # disclaimer()

if __name__ == "__main__":
    main()