from tensorflow.keras.metrics import categorical_accuracy, top_k_categorical_accuracy

def metrics(): 
    
    """ 
       A metric is a function that is used to judge the performance of your model.
        Metric functions are to be supplied in the metrics parameter when a model is compiled.
    """
    
        # Define Top2 and Top3 Accuracy

    def top_3_accuracy(y_true, y_pred):
        return top_k_categorical_accuracy(y_true, y_pred, k=3)

    def top_2_accuracy(y_true, y_pred):
        return top_k_categorical_accuracy(y_true, y_pred, k=2)
    
    
    metrics = [categorical_accuracy, 
               top_3_accuracy,
               top_2_accuracy \
              ]
    
    
    return metrics


if __name__ == '__main__':

    import sys
    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    metrics()

    
    