from tensorflow import keras
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import ModelCheckpoint
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# MNIST podatkovni skup
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train_s = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test_s = x_test.reshape(-1, 28, 28, 1) / 255.0

y_train_s = to_categorical(y_train, num_classes=10)
y_test_s = to_categorical(y_test, num_classes=10)

# Strukturiraj konvolucijsku neuronsku mrezu
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Definiraj karakteristike procesa ucenja pomocu .compile()
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Definiraj callbacks
checkpoint = ModelCheckpoint('best_model.h5', save_best_only=True, monitor='val_loss', mode='min')

# Provedi treniranje mreze pomocu .fit()
history = model.fit(x_train_s, y_train_s, epochs=10, batch_size=32,
                    validation_split=0.2, callbacks=[checkpoint])

# Ucitaj najbolji model
best_model = keras.models.load_model('best_model.h5')

# Izracunajte tocnost mreze na skupu podataka za ucenje i skupu podataka za testiranje
train_loss, train_acc = best_model.evaluate(x_train_s, y_train_s, verbose=0)
test_loss, test_acc = best_model.evaluate(x_test_s, y_test_s, verbose=0)

print(f'Točnost na skupu za učenje: {train_acc:.4f}')
print(f'Točnost na skupu za testiranje: {test_acc:.4f}')

# Prikazite matricu zabune na skupu podataka za testiranje
y_pred = np.argmax(best_model.predict(x_test_s), axis=1)
y_true = np.argmax(y_test_s, axis=1)

conf_matrix = confusion_matrix(y_true, y_pred)
plt.figure(figsize=(10, 8))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=range(10), yticklabels=range(10))
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()
