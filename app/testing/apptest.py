import streamlit as st
from streamlit_searchbox import st_searchbox
import pandas as pd
from functools import partial
from datetime import date,datetime,time,timedelta,datetime

#st.markdown("""
#<style>
#body, html {
#    direction: RTL;
#    unicode-bidi: bidi-override;
#    text-align: center;
#}
#p, div, input, label, h1, h2, h3, h4, h5, h6 {
#    direction: RTL;
#    unicode-bidi: bidi-override;
#    text-align: center;
#}
#</style>
#""", unsafe_allow_html=True)


#streamlit run apptest.py
# A function that filters a list of items based on the user query
def search_function(searchterm: str):
    df = pd.read_excel('eventDB.xlsx')

    # Access data from a specific column
    all_supplier_names = df['שם הספק'].values
    unique_supplier_names = sorted(set(all_supplier_names))
    #print(unique_supplier_names[1][::-1])
    return [item for item in unique_supplier_names if searchterm.lower() in item.lower()]

def q_search_function(searchterm: str,supplier):
    df = pd.read_excel('eventDB.xlsx')
    filtered_df = df[df["שם הספק"] == supplier]
    # Access data from a specific column
    all_supplier_names = filtered_df['סוג השירות'].values
    unique_supplier_names = sorted(set(all_supplier_names))
    #print(unique_supplier_names[1][::-1])

    return [item for item in unique_supplier_names if searchterm.lower() in item.lower()]

def testing(): # working! - get numbers & call and show when nedded..
    # Example: Integer input
    st.subheader("Integer Input Example")
    int_num = st.number_input(
    "Enter an integer (0 to 10)",
    min_value=0, # Setting min/max as integers forces integer input
    max_value=10,
    step=1,
    value=0
    )
    st.write("Entered integer:", int_num)

    start_date, end_date = st.date_input(
    "Select a date range",
    value=(date.today(), date.today()),
    min_value=date(2000, 1, 1),
    max_value=date(9999, 12, 31)
    )

    st.write(f"Start date: {start_date}")
    st.write(f"End date: {end_date}")
    how_long = end_date - start_date 
    st.write(f"the event is {how_long.days + 1} days long..")

    with st.form(key='my_form'):
        st.write("Inside the form")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
    # Grouping more inputs horizontally inside the form
        col_a, col_b = st.columns(2)
        with col_a:
            event_name = st.text_input("שם האירוע:")
            unit = st.text_input("שם היחידה:")
        with col_b:
            dd = st.text_input("שם d:")
    
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        st.success(f"Form submitted with Username: {username}, Date: {date}, Time: {time}")


    c1, c2, c3 = st.columns(3)
    c4, c5, c6 = st.columns([6,3,2]) #just to highlight these are different cols

    with st.container():
        event_comander_name = st.text_input("שם מפקד האירוע")
        event_comander_role = st.text_input("תפקיד המפקד")
        event_comander_phone = st.text_input("מפקד - מס' טלפון")

    with st.container():
        event_contact_name = st.text_input("שם איש הקשר")
        event_contact_role = st.text_input("תפקיד איש הקשר")
        event_contact_phone = st.text_input("איש קשר - מס' טלפון")
    

        
    new_row_data = {'שעה': a, 'תוכנית': b, 'מיקום': c, 'הערה': d}
    new_row_df = pd.DataFrame([new_row_data]) # Must be in a list to create a DataFrame
    new_data = pd.concat([df, new_row_df], ignore_index=True)
    return new_data
    # Loop to create rows of input widgets


    num_rows = st.slider('Number of rows', min_value=1, max_value=15)
    data = {}
    df = pd.DataFrame(data)   
    for r in range(num_rows):
        df = add_row(r,df)


    st.dataframe(df)

    temp = st.text_input("something")

    data = {'Name': ['Tom', 'Mike', 'Kate'], 'Age': [25, 30, 35]}
    df = pd.DataFrame(data) # Default integer index (0, 1, 2)
    df.iat[1, 1] = 31

    st.write(df.iat[1, 1])
    df.iat[1, 1] = temp

    st.table(df)

    new_row_data = {'Name': 'Charlie', 'Age': 35}
    new_row_df = pd.DataFrame([new_row_data]) # Must be in a list to create a DataFrame
    df = pd.concat([df, new_row_df], ignore_index=True)


    df.iat[1, 1] = 45

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

q_selected_value = False

st.title("V0.0.2 Demo")


    # columns to lay out the inputs


    # Function to create a row of widgets (with row number input to assure unique keys)

df = pd.read_excel('eventDB.xlsx')
# Access data from a specific column
all_supplier_names = df['שם הספק'].values
unique_supplier_names = sorted(set(all_supplier_names))


t = st.time_input("Set an alarm for", value = None)
st.write("Alarm is set for", t)

appointment_range = st.slider(
    "Select your desired hours range:",
    min_value=time(0, 0),
    max_value=time(23, 59),
    value=(time(9, 0), time(9, 0)),
    step=timedelta(minutes=5),
    format="HH:mm" # Optional: specifies the display format for the times
)

# The result is a tuple containing the start and end times
start_time, end_time = appointment_range
st.write("You selected a time range from:", start_time.strftime("%I:%M %p"), "to", end_time.strftime("%I:%M %p"))



# Pass the search function to the component
selected_value = st_searchbox(
    search_function,
    key="supplier",
    placeholder="Search for a supplier...",
)

st.write(f"Selected/Typed value: {selected_value}")

# Pass the search function to the component
if(selected_value):
    search_with_params = partial(q_search_function, supplier=selected_value)
    q_selected_value = st_searchbox(
        search_with_params,
        key="event",
        placeholder="Search for a event...",
    )

if(q_selected_value):
    df = pd.read_excel('eventDB.xlsx')
    filtered_df = df[(df["שם הספק"] == selected_value) & (df["סוג השירות"] == q_selected_value)] 
    # Access data from a specific column
    no_mam = filtered_df['מחיר ללא מעמ'].values
    yes_mam = filtered_df['מחיר (כולל מעמ)'].values
    all_o_names = (no_mam,yes_mam)

    st.write(f"Selected/Typed value: {all_o_names}")

if(q_selected_value):
    df = pd.read_excel('eventDB.xlsx')
    filtered_df = df[(df["שם הספק"] == selected_value) & (df["סוג השירות"] == q_selected_value)] 
    # Access data from a specific column
    stut = filtered_df['סטטוס'].values
    do_mam = filtered_df['האם משלם מעמ'].values
    misc = (stut,do_mam)

    st.write(f"Selected/Typed value: {misc}")

event = (selected_value,q_selected_value)
if event[0] == "ויטמין שיא בעמ":
    testing()
else: # alwase with if-else.. else-erorr.
    st.write("nothing")

st.write(f"Selected/Typed value: {q_selected_value}")

