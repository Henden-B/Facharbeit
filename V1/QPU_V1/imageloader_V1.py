import tensorflow.keras as ks
import numpy as np
import matplotlib.pyplot as plt

def getImageandPad(show_image=False):
    print('Process Started') #Start Meldung

    #Load important stuff
    (x_train,y_train), (x_test,y_test) = ks.datasets.mnist.load_data()
    rand_idx = np.random.randint(0, len(x_train)-1)

    image = x_train[rand_idx]
    label = y_train[rand_idx]
    print('currently working on a image like: ', label)

    padded_image = np.pad(image, pad_width=4, mode='constant', constant_values=0)
    normalized_image = padded_image / 255.0

    # Bild anzeigen nur wenn true
    if(show_image == True):
        plt.figure(figsize=(2, 2))
        plt.imshow(padded_image, cmap='gray')
        plt.title(f'Label: {label}')
        plt.axis('off')
        plt.show()

    return normalized_image

if(__name__ == '__main__'):
    getImageandPad(True)

