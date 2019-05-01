import tensorflow

def gen_callbacks(***kwargs): 
    
    """ 
        A callback is a set of functions to be applied at given stages of the training procedure. 
        Use callbacks to get a view on internal states and statistics of the model during training. 
    """
     #args
    filepath = kwargs['filepath']
    monitor  = kwargs['monitor']
        
    #callbacks
    checkpoint = tensorflow.keras.ModelCheckpoint(filepath, monitor = monitor, verbose=1, 
                             save_best_only=True, mode='max')

    reduce_lr = tensorflow.keras.ReduceLROnPlateau(monitor = monitor, factor=0.5, patience=2, 
                                   verbose=1, mode='max', min_lr=0.00001)
                                                            
    callbacks = [checkpoint, reduce_lr]
    
    return callbacks

if __name__ == '__main__':

    import sys
    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    print(gen_callbacks())

    
    
    