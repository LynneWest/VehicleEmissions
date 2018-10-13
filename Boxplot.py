#Create boxplot to answer question A
import pyodbc
import matplotlib.pyplot as plt
import numpy as np

conn_str = (
    r'DRIVER={SQL Server};'
    r'SERVER=DESKTOP-DK5R027\SQLEXPRESS;'
    r'DATABASE=VehEm;'
    r'Trusted_Connection=yes;' )
cnxn = pyodbc.connect(conn_str)
cur = cnxn.cursor()

query_string = "SELECT co2TailpipeGpm FROM vehicle WHERE fuelType2 IS NULL AND atvType IS NULL AND fuelType1 != 'Natural Gas' AND fuelType1 != 'Electricity' AND fuelType1 != 'Diesel' AND VClass ="

cc = cur.execute(query_string + "'Compact Cars';")
cc = np.array(cc.fetchall())

lc = cur.execute(query_string + "'Large Cars';")
lc = np.array(lc.fetchall())

mc = cur.execute(query_string + "'Midsize Cars';")
mc = np.array(mc.fetchall())

minc = cur.execute(query_string + "'Minicompact Cars';")
minc = np.array(minc.fetchall())

spt = cur.execute(query_string + "'Small Pickup Truck';")
spt = np.array(spt.fetchall())



data = [cc,lc,mc, minc, spt]

fig, ax1 = plt.subplots()
label = ['Compact Cars','Large Cars','Midsize Cars','Minicompact Cars','Small Pickup Trucks']
plt.boxplot(data, vert=False)
ax1.set_yticklabels(label)
plt.show()
