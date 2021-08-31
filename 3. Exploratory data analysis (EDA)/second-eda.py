import matplotlib.pyplot as plt
import pandas as pd

data = {'Nuts': [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
        'Chocolate': [85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5],
        'Preference': [10.5, 9.84, 25.64, 8.6, 7.98, 7.32, 6.7, 6.23, 5.51, 5.0, 4.73, 0.5, 0.45, 0, 0, 0, 1]}

df = pd.DataFrame(data)

plt.scatter(df['Chocolate'], df['Preference'])
plt.plot(df['Chocolate'], 0.12 * df['Chocolate'] + 0.13, 'g-')
plt.grid()
plt.xlabel('Chocolate Proportion')
plt.ylabel('Preference')