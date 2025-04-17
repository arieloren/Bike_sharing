import pandas as pd

class LoadPredictions:
    def __init__(self, config):
        self.config = config


    def save_with_predictions(self, original_df, predictions):
        df_with_predictions = original_df.copy()
        df_with_predictions["prediction"] = predictions
        df_with_predictions.to_csv(self.config.RESULT_FILE_PATH, index=False)
