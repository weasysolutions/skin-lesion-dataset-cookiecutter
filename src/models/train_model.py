import os, sys, inspect

 # Use this if you want to include modules from a subfolder        
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"gen_callbacks")))
if cmd_subfolder not in sys.path:
    sys.path.append(cmd_subfolder)     

cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"gen_class_weights")))
if cmd_subfolder not in sys.path:
    sys.path.append(cmd_subfolder)        
        
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"gen_metrics")))
if cmd_subfolder not in sys.path:
    print('appended sys path',cmd_subfolder)
    sys.path.append(cmd_subfolder)         
        
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"gen_model")))
if cmd_subfolder not in sys.path:
    print('appended sys path',cmd_subfolder)
    sys.path.append(cmd_subfolder)     
        
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"gen_batches")))
if cmd_subfolder not in sys.path:
    print('appended sys path',cmd_subfolder)
    sys.path.append(cmd_subfolder)
    
from gen_batches import hola_que_hace        
from gen_model import gen_model
from gen_batches import gen_batches
from gen_class_weights import gen_class_weights
from gen_metrics import gen_metrics
from gen_model import gen_model 
from gen_steps import gen_steps

def train_model(**kwargs): 
    
    """ 
        Machine Learning Training Tasks
    """
    
    #paths
    train_path = kwargs['train_path']
    valid_path = kwargs['valid_path']
    file_path  = kwargs['file_path']
    
    train_batch_size = kwargs['train_batch_size']
    val_batch_size = kwargs['val_batch_size']
    
      
    # three types of batches: validation, train, test    
    print(gen_batches)
    hola_que_hace(hola_que_hace = 'hola que onda')
    #batches = gen_batches( train_path = train_path,
    #                       valid_path = valid_path,
    #                       image_size = 224,
    #                       train_batch_size = train_batch_size,
     #                      val_batch_size = val_batch_size \
     #                    )  
    
    #list of metrics
      # val_top_2_accuracy, val_top_3_accuracy, categorical_accuracy
    metrics = gen_metrics()
    
    #list of class_weights
    class_weights = gen_class_weights(class_indices = batches['train'].class_indices)
    
    # steps
    steps_per_epoch, validation_steps = gen_steps(train_dir = train_path,
                                          val_dir = val_path,
                                          train_batch_size = train_batch_size,
                                          val_batch_size = val_batch_size \
                                          )
    
    print('steps_per_epoch',steps_per_epoch)
    print('validation_steps',validation_steps)
    
    # batch_size determines the number of samples in each mini batch. 
    # steps_per_epoch the number of batch iterations before a training epoch is considered finished.
    # validation_steps similar to steps_per_epoch but on the validation data set instead on the training data.
    
    #keras model                            
    model = gen_model()
    
    model.compile(Adam(lr=0.01), loss='categorical_crossentropy', 
              metrics=metrics)
                                   
    #list of callbacks                             
    callbacks = gen_callbacks(file_path = file_path, monitor = 'val_top_3_accuracy')
   
    history = model.fit_generator(batches['train'], 
                             steps_per_epoch = steps_per_epoch, 
                              class_weight = class_weights,
                               validation_data = batches['validation'],
                                validation_steps = validation_steps,
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

    
    
    