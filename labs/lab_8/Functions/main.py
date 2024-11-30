from data_loader import DataLoader
from data_analysis import DataAnalysis
from visualizer import Visualizer

file_path = '/Users/user/train.csv'
data_loader = DataLoader(file_path)
data = data_loader.load_data()

print("Перегляд перших рядків даних:")
print(data.head())

data_analysis = DataAnalysis(data)
min_values, max_values = data_analysis.get_min_max_values()
print("\nМінімальні значення по стовпцях:\n", min_values)
print("Максимальні значення по стовпцях:\n", max_values)

filtered_data = data_analysis.filter_data('Age', 20)

visualizer = Visualizer(filtered_data)
visualizer.basic_bar_chart()
visualizer.scatter_plot()
visualizer.multiple_subplots()

visualizer.save_visualization('visualization')
