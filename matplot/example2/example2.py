from matplotlib import pyplot as plt
import numpy as np

#plt.style.use('fivethirtyeight')

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_index = np.arange(len(ages_x))
barwidth = 0.25

# python devs #
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

pythonFmt="b"   # blue
plt.bar(x_index - barwidth, py_dev_y, width=barwidth, label="Python")
#plt.plot(ages_x, py_dev_y, color='b', linewidth=3, marker="o", label="Python")


# js devs #
js_dev_y = [37810, 43515, 46823, 49293, 53437, 
            56373, 62375, 66674, 68745, 68746, 74583]
#plt.plot(ages_x, js_dev_y, color='#adad3b', linewidth=3, marker="o", label="Javascript")
plt.bar(x_index, js_dev_y, width=barwidth, label="Javascript")


# all devs #
dev_y = [38496, 42000, 46752, 49320, 53200, 
         56000, 62316, 64928, 67317, 68748, 73752]

plt.bar(x_index + barwidth, dev_y, color="#444444", width=barwidth, label="All Devs")

plt.title("Median Salary (USD) by Age")

plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

# add legend
plt.legend()

plt.xticks(ticks=x_index, labels=ages_x)

#plt.grid(True)
plt.tight_layout()

plt.savefig('plot.png')

plt.show()
