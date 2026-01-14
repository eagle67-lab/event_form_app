import streamlit as st
from streamlit_searchbox import st_searchbox
import pandas as pd
from functools import partial
from datetime import date,datetime,time,timedelta
from TypeCast import *
from fileMaker import *
import time

def get_location(): # add selectbox for base \ free \ pay spase.
    location = st.text_input(":מיקום האירוע")
    return location

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
   
    return event_name,unit,full_date,event_comander,event_contact

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

def create_supplier_list(searchterm: str):

    df = pd.read_excel('eventDB.xlsx')
    all_supplier_names = df['שם הספק'].values
    unique_supplier_names = sorted(set(all_supplier_names))

    return [item for item in unique_supplier_names if searchterm.lower() in item.lower()]

def create_activity_list(searchterm: str,supplier):

    df = pd.read_excel('eventDB.xlsx')
    filtered_df = df[df["שם הספק"] == supplier]
    all_supplier_names = filtered_df['סוג השירות'].values
    unique_supplier_names = sorted(set(all_supplier_names))

    return [item for item in unique_supplier_names if searchterm.lower() in item.lower()]

def get_price(chosen_activity,supplier):

    df = pd.read_excel('eventDB.xlsx')
    filtered_df = df[(df["שם הספק"] == supplier) & (df["סוג השירות"] == chosen_activity)] 

    regular_price = filtered_df['מחיר ללא מעמ'].values
    full_price = filtered_df['מחיר (כולל מעמ)'].values

    return (regular_price,full_price)

def get_extra_data(chosen_activity,supplier):

    df = pd.read_excel('eventDB.xlsx')
    filtered_df = df[(df["שם הספק"] == supplier) & (df["סוג השירות"] == chosen_activity)] 

    group_type = filtered_df['סטטוס'].values
    pay_type = filtered_df['האם משלם מעמ'].values

    return (group_type,pay_type)

def rules():
    pass
    #return recommend_status

def disclaimer():
    pass
    #return check

def collect_activity(num_id):
    curent_activity = Activity()
    chosen_supplier = False
    chosen_activity = False
    chosen_supplier = st_searchbox(create_supplier_list,key="supplier",placeholder="Search for a supplier...",)
    if(chosen_supplier): #add dinamic ID on st_searchbox call
        full_func = partial(create_activity_list, supplier=chosen_supplier)
        chosen_activity = st_searchbox(full_func,key="event",placeholder="Search for a event...",)
    if(bool(chosen_supplier) & bool(chosen_activity)):
        price_block = get_price(chosen_activity,chosen_supplier)
        extra_data = get_extra_data(chosen_activity,chosen_supplier)
        curent_activity.update_data(num_id,chosen_supplier,chosen_activity,price_block[0],extra_data[0],extra_data[1])
    else:
        curent_activity = Activity() #reset buffer on cancel, remove when work on multipal activitys.

    return curent_activity

def add_row(row,df):
    grid = st.columns(4)
    with grid[0]:
        d = st.text_input('הערה', key=f'input_col4{row}')
    with grid[1]:
        c = st.text_input('מיקום', key=f'input_col3{row}')
    with grid[2]:
        b = st.text_input('תוכנית', key=f'input_col2{row}')
    with grid[3]:
        a = st.time_input('זמן', key=f'input_col1{row}')
        a = a.strftime('%H:%M')

    new_row_data = {'hour': a, 'plan': b, 'locaition': c, 'note': d}
    new_row_df = pd.DataFrame([new_row_data]) # Must be in a list to create a DataFrame
    new_data = pd.concat([df, new_row_df], ignore_index=True)

    return new_data

def build_schedule():
    #node = [time_point,contents,place,remark]
    #headers = ["שעה", "תוכנית", "מיקום", "הערה"]
    num_rows = st.slider('Number of rows', min_value=1, max_value=15)
    data = {}
    full_schedule = pd.DataFrame(data)   
    for r in range(num_rows):
        full_schedule = add_row(r,full_schedule)

    st.dataframe(full_schedule)

    return full_schedule

def main():
    st.write("!ברוך הבא")
    my_form = Forms()
    check = welcome()
    if (check): 
        event_name,unit,full_date,event_comander,event_contact = get_dry_data()
        event_location = get_location()
        guest_count = get_guest_count()
        main_activity = collect_activity(1)
        event_schedule = build_schedule()

        my_form.update_data(
            (event_name,unit), #user
            main_activity, #activitys
            guest_count, #guests
            full_date, #dates
            (event_comander,event_contact), #personals
            event_schedule, #schedule
            event_location #location
        )

        
        if st.button("הכן קובץ להורדה!"):
            with st.spinner("נאפה בתנור..."):
                time.sleep(5)
                complite_print(my_form)
            st.markdown("תודה רבה")
        
        #disclaimer()

if __name__ == "__main__":
    main()
