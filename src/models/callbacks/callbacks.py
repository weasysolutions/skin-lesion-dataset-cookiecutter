from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint

def callbacks(***kwargs): 
    
    """ 
        A callback is a set of functions to be applied at given stages of the training procedure. 
        Use callbacks to get a view on internal states and statistics of the model during training. 
    """
     
        filepath = kwargs['filepath']
        monitor  = kwargs['monitor']
        
        filepath = "model.h5"
checkpoint = tensorflow.keras.ModelCheckpoint(filepath, monitor = monitor, verbose=1, 
                             save_best_only=True, mode='max')

reduce_lr = tensorflow.keras.ReduceLROnPlateau(monitor = monitor, factor=0.5, patience=2, 
                                   verbose=1, mode='max', min_lr=0.00001)
                              
                              
callbacks_list = [checkpoint, reduce_lr]

history = model.fit_generator(train_batches, steps_per_epoch=train_steps, 
                              class_weight=class_weights,
                    validation_data=valid_batches,
                    validation_steps=val_steps,
                    epochs=30, verbose=1,
                   callbacks=callbacks_list)
    
    model.compile(Adam(lr=0.01), loss='categorical_crossentropy', 
              metrics=metrics)
    
    return batches



if __name__ == '__main__':

    import sys
    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    train_model(sys.argv[1])

    
    
    
        
    
    model.compile(Adam(lr=0.01), loss='categorical_crossentropy', 
              metrics=metrics)
    
    return batches



if __name__ == '__main__':

    import sys
    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    train_model()

    
    
    