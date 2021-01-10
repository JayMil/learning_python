from matplotlib import pyplot as plt

#print(plt.style.available)
#plt.style.use('fivethirtyeight')
#plt.style.use(plt.style.available[2])

plt.xkcd()

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]


# python devs #
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

pythonFmt="b"   # blue
plt.plot(ages_x, py_dev_y, label="Python")
#plt.plot(ages_x, py_dev_y, color='b', linewidth=3, marker="o", label="Python")


# js devs #
js_dev_y = [37810, 43515, 46823, 49293, 53437, 
            56373, 62375, 66674, 68745, 68746, 74583]
#plt.plot(ages_x, js_dev_y, color='#adad3b', linewidth=3, marker="o", label="Javascript")
plt.plot(ages_x, js_dev_y, label="Javascript")


# all devs #
dev_y = [38496, 42000, 46752, 49320, 53200, 
         56000, 62316, 64928, 67317, 68748, 73752]

allDevsFmt="k--"    # black with dotted line
plt.plot(ages_x, dev_y, color="#444444", linestyle='--', label="All Devs")

plt.title("Median Salary (USD) by Age")

plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

# add legend
plt.legend()

#plt.grid(True)
plt.tight_layout()

plt.savefig('plot.png')

plt.show()
