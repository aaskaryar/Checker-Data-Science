#Aria Askaryar Trash checker
#uses C:\Users\GisUser\Desktop\Aria\TRASH-TEMPLATE.xlsx

import pandas as pd
from pandas import DataFrame

trash = pd.read_excel("C:/Users/GisUser/Desktop/Aria/TRASH-TEMPLATE.xlsx", sheet_name='SiteInformation')
trash.columns = trash.columns.str.lower()

#To test if Start time and end time is correct True and False
badtime = trash.StartTime > trash.EndTime

goodtime = trash.StartTime < trash.EndTime

#Shows all rows which either has good rows which means start time is before end time 
#or
#shows all the bad rows which is where start time is after end time

badrows = trash[trash['StartTime'] > trash['EndTime']]

goodrows = trash[trash['StartTime'] < trash['EndTime']]
