#Aria Askaryar Trash checker
#uses C:\Users\GisUser\Desktop\Aria\TRASH-TEMPLATE.xlsx

import pandas as pd
from pandas import DataFrame

trash = pd.read_excel("C:/Users/GisUser/Desktop/Aria/TRASH-TEMPLATE.xlsx", sheet_name='SiteInformation')
#trash.columns = trash.columns.str.lower()

#To test if Start time and end time is correct True and False
badtime = trash.StartTime > trash.EndTime

goodtime = trash.StartTime < trash.EndTime

#testing to see good rows where start is before end
goodrows = trash[trash['StartTime'] < trash['EndTime']].index.tolist()

#checker, for if start time is after end time
badrows = trash[trash['StartTime'] > trash['EndTime']].index.tolist()
