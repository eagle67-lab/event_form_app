

class Activity:
    def __init__(self):
        self.id = ""
        self.supplier_name = ""
        self.activity_name = ""
        self.regular_price = 0
        self.group_type = ""
        self.pay_type = ""
    
    def update_data(self,id,supplier_name,activity_name,regular_price,group_type,pay_type):
        self.id = id
        self.supplier_name = supplier_name
        self.activity_name = activity_name
        self.regular_price = regular_price
        self.group_type = group_type
        self.pay_type = pay_type


class Forms:
    def __init__(self):

        self.user = []
        self.activitys = [] # list of events
        self.guests = {} #dict
        self.dates = ()
        self.personals = []
        self.schedule = []
        self.locaition = ""

    def add_event(self,new_activity):
        # add to list - self.activitys
        pass

    
    def update_data(self,user,activitys,guests,dates,personals,schedule,locaition):
        self.user = user
        self.activitys = activitys # list of events
        self.guests = guests #dict
        self.dates = dates
        self.personals = personals
        self.schedule = schedule
        self.locaition = locaition




my_form = Forms() 
my_form.user = "hiii"
print(my_form.user)