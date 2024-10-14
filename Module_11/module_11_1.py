import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


x = [i for i in range(2014, 2025)]  # года с 2014 по 2024
y = [35.5, 36.13, 37.6, 40.1, 43.95, 45.67, 46.2, 48.5, 51.35, 54.87, 58.65] # цены на АИ-95


plt.figure(figsize=(10, 7))
# plt.bar(x, y, width=0.1)
plt.suptitle('Динамика цен АИ-95 за последние 10 лет', fontsize=16)
plt.plot(x, y)
plt.xticks(x)
plt.yticks(y)
# plt.savefig('Fuel.png')  # строка нужна при использовании matplotlib.use('Agg')
plt.show()
