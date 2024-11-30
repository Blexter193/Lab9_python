class DataAnalysis:
    def __init__(self, data):
        self.data = data

    def get_min_max_values(self):
        numeric_data = self.data.select_dtypes(include=['float64', 'int64'])
        min_values = numeric_data.min()
        max_values = numeric_data.max()
        return min_values, max_values

    def filter_data(self, column_name, threshold_value):
        if column_name in self.data.columns:
            return self.data[self.data[column_name] > threshold_value]
        return self.data
