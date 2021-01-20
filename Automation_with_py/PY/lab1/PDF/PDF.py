#we have a dict and going to turn it into pdf report
fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}
from reportlab.platypus import SimpleDocTemplate
report = SimpleDocTemplate("/tmp/report.pdf")  #report will be created here

from reportlab.platypus import Paragraph, Spacer, Table, Image #create a title, some text in paragraphs, and some charts and images.

from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet() #to tell reportlab what style we want 
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"]) #to give this report a title!
#report.build([report_title])    #--> to built PDF with title

table_data = []
for k, v in fruit.items():
  table_data.append([k, v]) #making list of lists in order to create a Table
#report_table = Table(data=table_data) #NOT NEEDED, can be ussed below


from reportlab.lib import colors
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)] # making frame 
report_table = Table(data=table_data, style=table_style, hAlign="LEFT") #moving to the left
#report.build([report_title, report_table])#--> to built PDF with title and table

from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
report_pie = Pie(width=3*inch, height=3*inch)

report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):  #creating 2 lists for Pie
  report_pie.data.append(fruit[fruit_name])
  report_pie.labels.append(fruit_name)

report_chart = Drawing()    #Assigning to Drawing
report_chart.add(report_pie)
report.build([report_title, report_table, report_chart])
