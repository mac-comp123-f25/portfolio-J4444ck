import seaborn as sns
import matplotlib.pyplot as plt

cars_df = sns.load_dataset('mpg')


sns.set_theme(style='whitegrid')

sns.violinplot(data=cars_df, x='origin', y='mpg')

plt.title('Distribution of Car Mileage (MPG) by Origin')
plt.xlabel('Car Origin')
plt.ylabel('Miles Per Gallon (MPG)')

plt.show()