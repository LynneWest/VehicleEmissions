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

cc = cur.execute("SELECT co2TailpipeGpm FROM vehicle WHERE VClass = 'Compact Cars'")
cc = np.array(cc.fetchall())

lc = cur.execute("SELECT co2TailpipeGpm FROM vehicle WHERE VClass = 'Large Cars'")
lc = np.array(lc.fetchall())

mc = cur.execute("SELECT co2Tailpipegpm FROM vehicle WHERE VClass = 'Midsize Cars'")
mc = np.array(mc.fetchall())



data = [cc,lc,mc]

fig, ax1 = plt.subplots()
label = ['Compact Cars','Large Cars','Midsize Cars']
plt.boxplot(data, showfliers=False, vert=False)
ax1.set_yticklabels(label)
plt.show()
