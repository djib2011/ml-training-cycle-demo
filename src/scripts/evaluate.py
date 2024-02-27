from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from utils import mlflow  # utils sets up tracking URL for mlflow


def evaluate_model(model, X_test, y_test):
    
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    metrics = {
           'accuracy': accuracy_score(y_test, y_pred),
           'precision': precision_score(y_test, y_pred),
           'recall': recall_score(y_test, y_pred), 
           'f1_score': f1_score(y_test, y_pred)
           }

    return metrics


def log_metrics_to_mlflow(metrics_dict, run_name):

    with mlflow.start_run(run_name=run_name):

        for name, value in metrics_dict.items():
            mlflow.log_metric(name, value)

