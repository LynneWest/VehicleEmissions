#Create boxplots to compare CO2 emissions by vehicle class
import pyodbc
import matplotlib.pyplot as plt
import numpy as np

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
label = ['Cars', 'Compact Cars', 'Sport Utility Vehicles', 'Trucks', 'Vans']
box = plt.boxplot(data, vert=False, patch_artist=True)
plt.setp(box['boxes'], facecolor='lightblue')
plt.setp(box['fliers'], markersize=3)
plt.setp(box['medians'], color='darkblue')
ax.set_xlim(100,1200)
plt.xticks([200,300,400,500,600,700,800,900,1000,1100])
ax.xaxis.grid(True, color='lightgrey')
ax.set_axisbelow(True)
ax.set_yticklabels(label)
ax.set_xlabel('Tailpipe CO2 in grams/mile')
ax.set_title('CO2 emissions by vehicle class')
plt.show()
