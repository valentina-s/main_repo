from spyre import server
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
                {"type" : "plot",
                "id":"show_plot",
                "control_id":"button2",
                "tab":"Plot",
                "on_page_load":False},
                {"type" : "table",
                  "id":"cost_table_id",
                  "control_id": "button3",
                  "tab": "Cost",
                  "on_page_load":False,
                }
                ]
                    #,{"type":"html","id":"html","control_id":"button1"}]
                    

    controls = [dict(type="button",
                     id = "button1",
                     label = "Load Schedule",
                     action_id = "table_id"),
                dict(type="button",
                     id = "button2",
                     label = "Show Plot",
                     action_id = "table_id"),
                dict(type="button",
                     id = "button3",
                     label = "Calculate Cost",
                     action_id = "table_id")]
    
    
    def getData(self, params):
        brokenBusID = params['brokenBusID']   
        # set a default filename so that I do not enter it every time
        if params['filename']=='':
            params['filename'] = 'fixed_width_file.csv'
        print(params['filename'])
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
        if brokenBusID not in data.Run.unique():
            print("This bus ID does not exist in today's schedule.")
            

        if  brokenBusID =='':
            return data
        else:
            #return data.loc[data['Run']==brokenBusID,]
            return pd.DataFrame(data.loc[data['Run']==brokenBusID,].BookingId.unique(),columns = ['BookingId'])
            
    def getPlot(self,params):
        df = self.getData(params)
        fig = plt.figure()
        splt1 = fig.add_subplot(2,1,1)
        splt1.plot(df.LAT)#,df.LON)
        splt2 = fig.add_subplot(2,1,2)
        splt2.plot(df['LON'])
        return fig
         
    
         
         
                  
         
         

app = SimpleApp()

app.launch()