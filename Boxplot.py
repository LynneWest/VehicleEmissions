#Create boxplots to compare CO2 emissions by vehicle class
import pyodbc
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

conn_str = (
    r'DRIVER={SQL Server};'
    r'SERVER=DESKTOP-DK5R027\SQLEXPRESS;'
    r'DATABASE=VClassCO2;'
    r'Trusted_Connection=yes;' )
cnxn = pyodbc.connect(conn_str)
cur = cnxn.cursor()

query_string = """SELECT co2TailpipeGpm 
                FROM vehicle 
                WHERE fuelType2 IS NULL 
                AND atvType IS NULL 
                AND fuelType1 != 'Natural Gas' 
                AND fuelType1 != 'Electricity' 
                AND fuelType1 != 'Diesel' 
                AND VClass ="""

car = cur.execute(query_string + "'Car';")
car = np.array(car.fetchall())

cc = cur.execute(query_string + "'Compact Car';")
cc = np.array(cc.fetchall())

suv = cur.execute(query_string + "'Sport Utility Vehicle';")
suv = np.array(suv.fetchall())

truck = cur.execute(query_string + "'Truck';")
truck = np.array(truck.fetchall())

van = cur.execute(query_string + "'Van';")
van = np.array(van.fetchall())

data = [car, cc, suv, truck, van]

fig, ax = plt.subplots()
box = ax.boxplot(data, vert=False, patch_artist=True, showfliers=False, whis=10)

label = ['Cars', 'Compact Cars', 'Sport Utility Vehicles', 'Trucks', 'Vans']

box_colors = ['thistle', 'mistyrose','lightskyblue', 'mediumaquamarine', 'peachpuff']
for patch, color in zip(box['boxes'], box_colors):
    patch.set_facecolor(color)

plt.setp(box['medians'], color='red')
plt.setp(box['caps'], color='blue')

lines = [Line2D([0], [0], color='red', label='median'),
Patch(facecolor='white',edgecolor='black', label='25% to 75%'),
Line2D([0], [0], color='blue', label='min and max')]

plt.legend(handles=lines)
ax.set_xlim(100,1200)
plt.xticks([200,300,400,500,600,700,800,900,1000,1100])
ax.xaxis.grid(True, color='lightgrey')
ax.set_axisbelow(True)
ax.set_yticklabels(label)
ax.set_xlabel('Tailpipe CO2 in grams per mile')
ax.set_title('CO2 Emissions by Vehicle Class')
plt.show()
