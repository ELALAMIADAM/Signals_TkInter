import sqlite3
connect=sqlite3.connect("signals.db")
cursor=connect.cursor()
query="SELECT x,y FROM samples WHERE signal_id='X';"
result=cursor.execute(query)
samples=[]
for sample in result :
    samples.append(sample)
X,Y = list(zip(*samples))
print(samples)
import matplotlib.pyplot as plt
plt.plot(X,Y)
plt.xlabel("time")
plt.ylabel("magnitude")

plt.show()
