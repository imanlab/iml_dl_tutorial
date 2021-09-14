import numpy as np
from tensorflow.keras.models import load_model

from data import load_dataset
from output import plot_confusion_matrix


# Load data.
(X_train, y_train), (X_test, y_test) = load_dataset(data_dir="data")

# Load the model from the saved file.
model = load_model('models/model.h5')

# Prediction.
y_test_pred = model(X_test)
# Convert from one-hot encoding to label (digit).
y_test_label = np.argmax(y_test, axis=1)
y_test_pred_label = np.argmax(y_test_pred, axis=1)

"""
Plot confusion matrix.

The confusion matrix represents the results of all predictions from our model and is useful to determine
both its general performance and specific problems (e.g. one digit could tend to be confused with another one).
"""
confusion_matrix = np.zeros((10, 10))
for label, pred_label in zip(y_test_label, y_test_pred_label):
    confusion_matrix[label, pred_label] += 1
confusion_matrix_norm = confusion_matrix / np.expand_dims(np.sum(confusion_matrix, axis=1), axis=-1)
plot_confusion_matrix(confusion_matrix_norm, range(10), range(10))

"""
Plot the confusion matrix with wrong predictions only.

This is obtained by removing the diagonal. This is not a canonical form of the confusion matrix, but it makes
it easier to see the colors and where wrong predictions accumulate if the network is really accurate.

An alternative would be to use logarithmic color scaling.
"""
confusion_matrix_errors_norm = confusion_matrix_norm - np.diag(np.diag(confusion_matrix_norm))
plot_confusion_matrix(confusion_matrix_errors_norm, range(10), range(10))

# Calculate prediction accuracy.
pred_correct = np.sum([confusion_matrix[i, i] for i in range(10)])
pred_total = len(y_test_pred)
acc = pred_correct / pred_total
print(f"Model accuracy: {acc:.4f}")
