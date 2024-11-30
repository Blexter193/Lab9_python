import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self, data):
        self.data = data

    def basic_bar_chart(self):
        if 'Pclass' in self.data.columns and 'Fare' in self.data.columns:
            plt.figure(figsize=(10, 6))
            plt.bar(self.data['Pclass'], self.data['Fare'])
            plt.xlabel('Клас пасажира')
            plt.ylabel('Вартість квитка')
            plt.title('Стовпчикова діаграма вартості квитка за класом')
            plt.show()
        else:
            print("Колонки 'Pclass' і 'Fare' відсутні, перейдіть до іншої візуалізації.")

    def scatter_plot(self):
        if 'Age' in self.data.columns and 'Fare' in self.data.columns:
            plt.figure(figsize=(10, 6))
            plt.scatter(self.data['Age'], self.data['Fare'], c='blue', alpha=0.5)
            plt.xlabel('Вік')
            plt.ylabel('Вартість квитка')
            plt.title('Діаграма розсіювання віку та вартості квитка')
            plt.show()
        else:
            print("Колонки 'Age' і 'Fare' відсутні для діаграми розсіювання.")

    def multiple_subplots(self):
        if 'Age' in self.data.columns and 'Fare' in self.data.columns and 'Survived' in self.data.columns:
            fig, axes = plt.subplots(1, 2, figsize=(14, 6))
            self.data.plot(kind='line', x='Age', y='Fare', ax=axes[0], title='Вік та вартість квитка')
            self.data.plot(kind='line', x='Age', y='Survived', ax=axes[1], title='Вік та виживання')
            plt.tight_layout()
            plt.show()
        else:
            print("Колонки 'Age', 'Fare' або 'Survived' відсутні для побудови кількох піддіаграм.")

    def save_visualization(self, filename):
        plt.savefig(f'{filename}.png')
        plt.savefig(f'{filename}.svg')
        print(f"Візуалізації збережено як '{filename}.png' та '{filename}.svg'")
