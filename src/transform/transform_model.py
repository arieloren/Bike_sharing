import pickle
from sklearn.ensemble import RandomForestClassifier


class TransformModel:
    def __init__(self, config):
        self.config = config
        self.models = {}  # Make sure it's 'models'
        self.__load_dependencies()

    def __validation(self, dataset):
        pass  # Add validation logic if needed

    def __load_dependencies(self):
        # Load casual model
        with open(self.config.model_casual, 'rb') as f:
            self.models["casual"] = pickle.load(f)

        # Load registered model
        with open(self.config.model_registered, 'rb') as f:
            self.models["registered"] = pickle.load(f)

    def Predict(self, dataset):
        # Use the models to make predictions
        casual = self.models["casual"].predict(dataset)
        registered = self.models["registered"].predict(dataset)

        return casual + registered
