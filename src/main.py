import config
from config import FILE_PATH
from extract.extract_base import ExtractBase
from extract.extract_file import ExtractFile
from transform.transform_model import TransformModel
from transform.transform_processing import TransformProcessing
from load.load_predictions import LoadPredictions
# from eval.model_evaluation import ModelEvaluation
def main():

    # Extract
    extract : ExtractBase = ExtractFile(FILE_PATH)
    dataset = extract.load_data()

    # transform
    transform = TransformProcessing(config)
    dataset_transform = transform.transform(dataset)

    # predict
    model = TransformModel(config)
    result = model.Predict(dataset_transform)

    # load
    print(result)
    # Save result with original data
    saver = LoadPredictions(output_path="output/predictions.csv")
    saver.save_with_predictions(dataset, result)


if __name__ == '__main__':
    main()

