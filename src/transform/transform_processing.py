import pickle
from math import sin, cos, pi

class TransformProcessing:
    
    def __init__(self, config):
        self.config = config
        # self.__load_dependency()  # Only include if needed

    def __explode_dt(self, df):

        df['year'] = df.index.year
        df['month'] = df.index.month
        df['hour'] = df.index.hour
        df['weekday'] = df.index.weekday
        return df

    def transform(self, dataset):

        dataset = self.__explode_dt(dataset)

        # dataset['hour_x'] = dataset['hour'].apply(lambda x: sin(2 * pi * x / 24))
        # dataset['hour_y'] = dataset['hour'].apply(lambda x: cos(2 * pi * x / 24))

        dataset.drop(self.config.drop_columns, axis=1, inplace=True)

        X = dataset[self.config.prdict_colunms]
        # y_casual = dataset['casual']
        # y_registered = dataset['registered']

        return X #,y_casual,y_registered

