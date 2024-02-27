from sklearn.datasets import make_circles


def make_circles_instance():
    """
    Make a single instance for the circles dataset
    """

    X, y = make_circles(n_samples=1, noise=0.1)
    X = X.tolist()[0]
    y = y.tolist()[0]

    return  X, y

def insert_instance_to_mongo_collection(x, y, collection):
    """
    Insert a single instance (x, y) to a mongo collection
    """
    
    data = {'features': x, 'labels': y}
    collection.insert_one(data)
    

def add_test_set_to_mongo():
    from utils import get_mongo_collection

    data = []
    for instance in zip(*make_circles(n_samples=500, noise=0.1)):
        x, y = instance
        data.append({'features': x.tolist(), 'labels': y.tolist()})

    collection = get_mongo_collection(train=False)
    collection.insert_many(data)


if __name__ == '__main__':

    from utils import get_mongo_collection

    collection = get_mongo_collection()
    x, y = make_circles_instance()
    insert_instance_to_mongo_collection(x, y, collection)

