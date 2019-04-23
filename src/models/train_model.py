
def train_model(**kwargs): 
    
    """ 
        Machine Learning Training Tasks
    """
    
    
    train_path = kwargs['train_path']
    valid_path = kwargs['valid_path']
    file_path  = kwargs['file_path']
    
    # three types of batches: validation, train, test    
    batches = generate_batches( \
                               train_path = train_path,
                               valid_path = valid_path,
                               train_batch_size = 10,
                               val_batch_size = 10,
                               image_size = 224 \
                              )  
    
    #list of metrics
      # val_top_2_accuracy, val_top_3_accuracy, categorical_accuracy
    metrics = metrics()
    
    #list of class_weights
    class_weights = class_weights(class_indices = batches['train'].class_indices)
    
    #keras model                            
    model =  model_architecture()
    
    model.compile(Adam(lr=0.01), loss='categorical_crossentropy', 
              metrics=metrics)
                                   
    #list of callbacks                             
    callbacks = callbacks(file_path = file_path, monitor = 'val_top_3_accuracy')
    
   
 
    history = model.fit_generator(batches['train'], 
                             steps_per_epoch = train_steps, 
                              class_weight = class_weights,
                               validation_data = batches['validation'],
                                validation_steps = val_steps,
                                 epochs = 30, 
                                  verbose = 1,
                                   callbacks=callbacks \
                                 )
    

    
    return batches



if __name__ == '__main__':

    import sys
    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    train_model(sys.argsv[1])

    
    
    