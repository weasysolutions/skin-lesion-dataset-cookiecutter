from tensorflow.keras.applications.mobilenet.preprocess_input import PreprocessInput
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def batches(**wkargs): 
    
    """ 
        Generate batches of tensor image data with real-time data augmentation.
        The data will be looped over (in batches).
    """
    
    train_path = wkargs['train_path']
    valid_path = wkargs['valid_path']
    num_train_samples = wkargs['num_train_samples']
    num_val_samples = wkargs['num_val_samples']
    train_batch_size = wkargs['train_batch_size']
    val_batch_size = wkargs['val_batch_size']
    image_size = wkargs['image_size']

    #Normalize with mobilenet preprocess input
    datagen = ImageDataGenerator(    
                   preprocessing_function = PreprocessInput )
    
    batches = {}
    
    batches['train'] = datagen.flow_from_directory(train_path,
                                            target_size=(image_size,image_size),
                                            batch_size=train_batch_size)

    batches['validation'] = datagen.flow_from_directory(valid_path,
                                            target_size=(image_size,image_size),
                                            batch_size=val_batch_size)

    # Note: shuffle=False causes the test dataset to not be shuffled
    batches['test'] = datagen.flow_from_directory(valid_path,
                                            target_size=(image_size,image_size),
                                            batch_size=1,
                                            shuffle=False)
    
    return batches


if __name__ == '__main__':

    import sys
    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    generate_batches(sys.argv[1])
