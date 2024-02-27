import os
import pickle
import shutil
import mlflow
from pymongo import MongoClient


MONGO_CONNECTION_STR = 'mongodb://localhost:27017/' 
DATABASE_NAME = 'ml_training_cycle_demo'
TRAIN_COLLECTION_NAME = 'circles_data_train'
TEST_COLLECTION_NAME = 'circles_data_test'

TEMP_DIR = '/tmp/pipeline_temp_dir'

mlflow.set_tracking_uri('http://localhost:5000') 
mlflow.set_experiment('circles_demo')


def get_mongo_collection(train=True):
    client = MongoClient(MONGO_CONNECTION_STR)
    db = client[DATABASE_NAME]
    collection = db[TRAIN_COLLECTION_NAME] if train else db[TEST_COLLECTION_NAME]

    return collection


def write_to_tempdir(filename, content):
    _create_tempdir_if_needed()

    with open(filename, 'wb') as f:
        pickle.dump(content, f)



def read_from_tempdir(filename):

    with open(filename, 'rb') as f:
        content = pickle.load(f)

    return content


def wipe_tempdir():
    shutil.rmtree(TEMP_DIR)


def _create_tempdir_if_needed():
    if not os.isdir(TEMP_DIR):
        os.makedirs(TEMP_DIR)


if __name__ == '__main__':

    collection = get_mongo_collection()

    print(f'Number of documents in collection {TRAIN_COLLECTION_NAME}: {collection.count_documents({})}')

