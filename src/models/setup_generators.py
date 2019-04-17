def setup_generators(**wkargs):        
    
    for sub in os.listdir(train_dir):
        
        num_train = len(os.listdir(os.path.join(train_dir,sub)))
        num_val = len(os.listdir(os.path.join(val_dir,sub)))