from collections import namedtuple


DataIngestionConfig = namedtuple("DataIngestionConfig",
["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_Train_dir","ingested_Test_dir"])

DataValidationConfig = namedtuple("DataValidationConfig",
['schema_file_path'])

DataTransformationConfig = namedtuple("DataTransformationConfig",
["add_bedroom_per_room","Transform_Train_dir","Transform_Test_dir","Transform_object_file_path"])

ModelTrainingConfig = namedtuple("ModelTrainingConfig",
["Train_model_file_path","base_accuracy"])

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",
"model_evaluation_file_path","time_stamp")

ModelPusherConfig = namedtuple("ModelPusherConfig",
["export_dir_path"])





