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

cur.execute("SELECT co2TailpipeGpm FROM vehicle WHERE VClass = 'Sport Utility Vehicle';")
data = np.array(cur.fetchall())
plt.boxplot(data, showfliers=False, vert=False)
plt.show()
