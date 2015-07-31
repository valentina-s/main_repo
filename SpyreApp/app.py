from spyre import server
import pandas as pd
import os

class SimpleApp(server.App):

    title = "Bus Rescheduling"

    inputs = [  dict(type = "text",
                        key = "filename",
                        label = "Enter the name of your schedule file"),
                dict(type = "text",                   
                   key = "brokenBusID",
                   label = "Enter the ID of the broken bus",
                   action_id="table_id")]
                   #,
                   #{"type":'radiobuttons',"options" : [
									#	{"label": "Cost", "value":1, "checked":True}]}
#										{"label":"Multiple Outputs", "value":2},
#										{"label":"Inputs with actions 1", "value":3},
#										{"label":"Inputs with actions 2", "value":4},
#		#        ]


    tabs = ["Table","Plot","Cost"]

    outputs = [{ "type" : "table",
                    "id" : "table_id",
                    "control_id" : "button1",
                    "tab" : "Table",
                    "on_page_load":False},
                {"type" : "table",
                "id":"cost_table_id",
                # "control_id":"button2",
                "tab":"Cost",
                "on_page_load":False}]
                    #,{"type":"html","id":"html","control_id":"button1"}]
                    

    controls = [dict(type="button",
                     id = "button1",
                     label = "Load Schedule",
                     action_id = "table_id"),
                dict(type="button",
                     id = "button2",
                     label = "Calculate Cost",
                     action_id = "cost_table_id")]
    
    
    def getData(self, params):
        brokenBusID = params['brokenBusID']    
    
        filename = os.path.join(os.getcwd(),'data',params['filename'])
        data = pd.read_csv(filename,sep = "\t")
        self.bus_number = data['Run']
        
    #def getHTML(self,params):
     #   return "These request ids needs to be served"
	
	# creating the list of options for the dropdown menu
	
	# listOfOptions = []
	# for item in data['Run']:
	# 	listOfOptions.append({label:item,value:item})
	
        #params['table1'] = True
	# check if brokenBusID is in today's list schedule
        if brokenBusID in data.Run.unique():
            print("This bus ID does not exist in today's schedule.")
            

        if  brokenBusID =='':
            return data
        else:
            return data.loc[data['Run']==brokenBusID,]
            # return data.loc[data['Run']==brokenBusID,'BookingId'].unique()

app = SimpleApp()

app.launch()