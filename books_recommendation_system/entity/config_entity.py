class DataIngestionConfig:
    def __init__(self, dataset_download_url: str, raw_data_dir: str, ingested_dir: str):
        self.dataset_download_url = dataset_download_url
        self.raw_data_dir = raw_data_dir
        self.ingested_dir = ingested_dir


class DataValidationConfig:
    def __init__(self, clean_data_dir: str, books_csv_file: str, ratings_csv_file: str, serialized_objects_dir: str):
        self.clean_data_dir = clean_data_dir
        self.books_csv_file = books_csv_file
        self.ratings_csv_file = ratings_csv_file
        self.serialized_objects_dir = serialized_objects_dir


class DataTransformationConfig:
    def __init__(self, clean_data_file_path: str, transformed_data_dir: str):
        self.clean_data_file_path = clean_data_file_path
        self.transformed_data_dir = transformed_data_dir


class ModelTrainerConfig:
    def __init__(self, transformed_data_file_dir: str, trained_model_dir: str, trained_model_name: str):
        self.transformed_data_file_dir = transformed_data_file_dir
        self.trained_model_dir = trained_model_dir
        self.trained_model_name = trained_model_name


class ModelRecommendationConfig:
    def __init__(self, book_name_serialized_objects: str, book_pivot_serialized_objects: str,
                 final_rating_serialized_objects: str, trained_model_path: str):
        self.book_name_serialized_objects = book_name_serialized_objects
        self.book_pivot_serialized_objects = book_pivot_serialized_objects
        self.final_rating_serialized_objects = final_rating_serialized_objects
        self.trained_model_path = trained_model_path
