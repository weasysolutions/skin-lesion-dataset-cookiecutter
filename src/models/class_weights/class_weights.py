def class_weights(**kwargs):
    
    class_indices = kwargs['class_indices']
    
    """ 
       Class weights in the NN
    """
    class_weights = {}
    
    #More sensitive to Melanoma.
    for key,value in class_indices.items():
        
        if value == 'mel'
            class_weights[key] = 3.0
        else:
            class_weights[key] = 1.0
        
    return class_weights
    

if __name__ == '__main__':

    import sys
    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    class_weights(sys.argv[1])
    
    