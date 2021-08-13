import numpy as np
import keras

def load_data(csv_path):
        # Load data from the CSV file.
        data = np.loadtxt(csv_path, delimiter=",")
        
        # Split data between input (first 9 columns) and output (last column).
        # Input.
        X = data[:, 0:8]
        # Output.
        y = data[:, 8]

        return X, y

"""
This is a really useful class for large datasets. For more information see:
https://stanford.edu/~shervine/blog/keras-how-to-generate-data-on-the-fly
"""
class DataGenerator(keras.utils.Sequence):

    def __init__(self, X, y, batch_size: int, shuffle: bool = True, random_state: int = None):
        
        # Initialize the random generator.
        # A seed can be provided to ensure reproducibility.
        self.rng = np.random.default_rng(random_state)
        self.shuffle = shuffle
        self.X = X
        self.y = y
        self.n_samples = self.y.shape[0]
        self.batch_size = batch_size
        self.indexes = np.arange(self.n_samples)

        self.on_epoch_end()

    def on_epoch_end(self):
        """Updates indexes after each epoch."""
        if self.shuffle:
            self.rng.shuffle(self.indexes)

    def __len__(self):
        """Denotes the number of batches per epoch."""
        return int(np.floor(self.n_samples/ self.batch_size))
    
    def __getitem__(self, index):
        """Generate one batch of data."""
        # Generate indexes of the batch
        indexes = self.indexes[index*self.batch_size:(index+1)*self.batch_size]

        # Generate data
        X, y = self.__data_generation(indexes)

        return X, y

    def __data_generation(self, indexes):
        X = self.X[indexes, :]
        y = self.y[indexes, :]

        return X, y
