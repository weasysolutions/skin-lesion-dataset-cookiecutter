import tensorflow

def model_architecture(): 
           
     # get mobilenet model

    mobile = tensorflow.keras.applications.mobilenet.MobileNet() 
            
    # MODEL ARCHITECTURE

    # Exclude the last 5 layers of the above model.
    # This will include all layers up to and including global_average_pooling2d_1
    x = mobile.layers[-6].output

    # Create a new dense layer for predictions
    # 7 corresponds to the number of classes
    x =  tensorflow.keras.layers.Dropout(0.25)(x)
    predictions =  tensorflow.keras.layers.Dense(7, activation='softmax')(x)

    # inputs=mobile.input selects the input layer, outputs=predictions refers to the
    # dense layer we created above.

    model = tensorflow.keras.models.Model(inputs=mobile.input, outputs=predictions)
    
    
    # Freeze the weights of all layers except the last 23 layers in the model.
    # The last 23 layers of the model will be trained.
    for layer in model.layers[:-23]:
        layer.trainable = False

    return model 


if __name__ == '__main__':

    import sys
    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    model_architecture()
