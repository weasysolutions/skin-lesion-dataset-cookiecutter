import os, sys

def gen_steps(**kwargs): 
    
    """ 
       Generate steps per epoch from batch size and number of train samples. 
       Similar for validation steps
    """
    
        # Args: training directory, validation directory, validation batch size, trainig batch size

    train_dir = kwargs['train_dir']
    val_dir = kwargs['val_dir']
    val_batch_size = kwargs['val_batch_size']
    train_batch_size = kwargs['train_batch_size']
    
    num_train_samples = len(os.listdir(train_dir))
    num_val_samples = len(os.listdir(val_dir))
    
    steps_per_epoch = num_train_samples // val_batch_size
    validation_steps = num_val_samples  // train_batch_size
    
    return steps_per_epoch, validation_steps


if __name__ == '__main__':

    import sys
    gen_steps(sys.argv[1])

    
    