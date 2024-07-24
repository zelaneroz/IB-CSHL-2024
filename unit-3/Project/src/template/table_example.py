from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from database_worker import database_worker


class TableScreen(MDScreen):
    #class variable
    data_table = None
    def on_pre_enter(self, *args):
        #b4 the screen is created the code is run
        self.data_table = MDDataTable(
            size_hint = (.8,.5),
            pos_hint = {"center_x":.5, "center_y":.5},
            use_pagination = False,
            check = True,
            #title of the columns
            column_data = [("id",40),
                           ("Sender ID",30),
                           ("Receiver ID",33),
                           ("Amount",30),
                           ("Hash",100)
                           ]
        )
        self.data_table.bind(on_row_press = self.row_pressed) # method name change so its more easy to understand
        self.data_table.bind(on_check_press = self.check_pressed)
        self.add_widget(self.data_table) #add table to the GUI
        self.update()

    def row_pressed(self,table,row):
        print("a row was pressed",row)

    def check_pressed(self, table, current_row):
        print("a check mark was pressed", current_row)

    #def save(self):
        #1 - get inputs from the MDTextFields
        #2 = INSERT into ledger
    def save(self):
        checked_rows = self.data_table.get_row_checks()
        print(checked_rows)
        #delete
        db = database_worker("bitcoin_exchange.db")
        for r in checked_rows:
            id=r[0]
            query = f"DELETE from ledger where id={id}"
            db.run_query(query)
        db.close()
        self.update()
    #def save(self): #save new data to database
    #    print("trying to save new tx")

    def update(self):
        #read database and update table
        db = database_worker("bitcoin_exchange.db")
        query = "SELECT * from ledger"
        data = db.search(query)
        db.close()
        self.data_table.update_row_data(None,data)

class table_example(MDApp):
    def build(self):
        pass

x = table_example()
x.run()