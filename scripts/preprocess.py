import numpy as np

from utils import get_mongo_collection


def fetch_data_from_mongo(train=True):
    
    collection = get_mongo_collection(train=train)

    return list(collection.find())


def process_mongo_documents(documents):

    X, y = [], []

    for document in documents:
        X.append(document['features'])
        y.append(document['labels'])

    return np.array(X), np.array(y)


if __name__ == '__main__':

    documents = fetch_data_from_mongo()
    print(f'{len(documents)} documents found in mongo')

    X, y = process_mongo_documents(documents)
    print(f'{X.shape = }  {y.shape = }')

