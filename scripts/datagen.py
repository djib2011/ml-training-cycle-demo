from sklearn.datasets import make_circles


def make_circles_instance():
    """
    Make a single instance for the circles dataset
    """

    X, y = make_circles(n_samples=1, noise=0.1, random_state=42)
    X = X.tolist()
    y = y.tolist()

    return  X, y


def insert_instance_to_mongo_collection(x, y, collection):
    """
    Insert a single instance (x, y) to a mongo collection
    """
    
    data = {'features': x, 'labels': y}
    collection.insert_one(data)
    

if __name__ == '__main__':

    from utils import get_mongo_collection

    collection = get_mongo_collection()
    x, y = make_circles_instance()
    insert_instance_to_mongo_collection(x, y, collection)

