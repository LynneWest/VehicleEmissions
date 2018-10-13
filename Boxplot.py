#Create boxplots to answer question A
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

sw = cur.execute(query_string + "'Station Wagon';")
sw = np.array(sw.fetchall())

truck = cur.execute(query_string + "'Truck';")
truck = np.array(truck.fetchall())

van = cur.execute(query_string + "'Van';")
van = np.array(van.fetchall())





data = [car, cc, suv, sw, truck, van]

fig, ax1 = plt.subplots()
label = ['Cars', 'Compact Cars', 'Sport Utility Vehicles', 'Station Wagons', 'Trucks', 'Vans']
plt.boxplot(data, vert=False)
ax1.set_yticklabels(label)
plt.show()
