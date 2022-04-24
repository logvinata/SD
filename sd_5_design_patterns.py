# -*- coding: utf-8 -*-
"""SD_5_design_patterns.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/191ZpbswX2tmlQl2DbXA8Ot_7fqk6iTq-
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

from sklearn.svm import SVC

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score

""" Фабричный метод отделяет код производства продуктов от остального кода, который эти продукты использует."""

class Factory:
    def __init__(self, X_train: np.ndarray, Y_train: np.ndarray):
        self.X_train = X_train
        self.Y_train = Y_train

    def get_subsample(self, df_share: int):
        """
        1. Copy train dataset
        2. Shuffle data (don't miss the connection between X_train and y_train)
        3. Return df_share %-subsample of X_train and y_train
        """
        X = self.X_train.copy()
        Y = self.Y_train.copy()

        X, Y = shuffle(X, Y, random_state=42)

        percentage = int(len(Y) * df_share / 100.0)

        return X[:percentage, :], Y[:percentage]

"""
1. Load iris dataset
2. Shuffle data and divide into train / test.
"""

X, Y = load_iris(return_X_y=True)
X, Y = shuffle(X, Y, random_state=42)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.75, random_state=42)

# print(f"Train size = {len(y_train)}, Test size = {len(y_test)}")

clf = make_pipeline(StandardScaler(), KNeighborsClassifier(7))

pattern_item = Factory(X_train, Y_train)
for df_share in range(10, 101, 5):
    curr_X_train, curr_y_train = pattern_item.get_subsample(df_share)

    clf.fit(curr_X_train, curr_y_train)

    Y_test_pred = clf.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_test_pred)

    print(f"df_share = {df_share}%, accuracy on test = {accuracy}")

"""
1. Preprocess curr_X_train, curr_y_train in the way you want
2. Train Linear Regression on the subsample
3. Save or print the score to check how df_share affects the quality
"""

# Outputs:
# df_share = 10%, accuracy on test = 0.8444444444444444
# df_share = 20%, accuracy on test = 0.9333333333333333
# df_share = 30%, accuracy on test = 0.9555555555555556
# df_share = 40%, accuracy on test = 0.9555555555555556
# df_share = 50%, accuracy on test = 0.9777777777777777
# df_share = 60%, accuracy on test = 0.9777777777777777
# df_share = 70%, accuracy on test = 0.9777777777777777
# df_share = 80%, accuracy on test = 0.9777777777777777
# df_share = 90%, accuracy on test = 0.9777777777777777
# df_share = 100%, accuracy on test = 0.9777777777777777

"""## Task 2

который предоставляет простой интерфейс к сложной системе классов, библиотеке или фреймворку.
"""

import numpy as np
# import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import accuracy_score

class Facade:
    def __init__(self, classifiers, *data) -> None:
        """
        Initialize a class item with a list of classificators
        """
        self.classifiers = classifiers
        self.X_train = X_train
        self.X_test = X_test
        self.Y_train = Y_train
        self.Y_test = Y_test


    
    def fit(self):
        """
        Fit classifiers from the initialization stage
        """
        # pipe = Pipeline(steps=[('scale', StandardScaler()), ('classifier', classifier)])
        # pipe.fit(X_train, Y_train)
            

    def predict(self, X_test):
        """
        Get predicts from all the classifiers and return
        the most popular answers
        """
            
        
        # return y_preds



    def get_best(self):

        y_preds = []

        for classifier in self.classifiers:
            pipe = Pipeline(steps=[('scale', StandardScaler()), 
                                   ('classifier', classifier)])
            pipe.fit(self.X_train, self.Y_train)

            scaler = StandardScaler()
            X_test = scaler.fit_transform(self.X_test)  #!?!? Why aren't they scaled automatically by pipeline??

            y_preds.append(classifier.predict(X_test))

            # print(classifier, y_preds[-1])

        y_preds = np.stack(y_preds)

        #most popular answers
        #scipy mode here?
        # print(y_preds)
        prediction = np.floor(y_preds.sum(axis=0) / len(self.classifiers) + 0.5).astype(int)
        
        return prediction



"""
1. Load iris dataset
2. Shuffle data and divide into train / test.
3. Prepare classifiers to initialize <StructuralPatternName> class.
4. Train the ensemble
"""
classifiers = [SVC(gamma='auto', random_state=42), 
               RandomForestClassifier(max_depth=5, random_state=42),
               KNeighborsClassifier(7),
               GaussianNB(),]

X, Y = load_iris(return_X_y=True)
X, Y = shuffle(X, Y, random_state=42)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, 
                                                           train_size=0.65, 
                                                           random_state=42)
data = X_train, X_test, Y_train, Y_test

ensemble = Facade(classifiers, data)

prediction = ensemble.get_best()

accuracy = accuracy_score(Y_test, prediction)

print(accuracy)

"""## Task 3

позволяет сохранять и восстанавливать прошлые состояния объектов, не раскрывая подробностей их реализации.
"""

import random

import random
from typing import List
from IPython.display import clear_output

def get_random_vector(n):
    """Return `n` floats from -1 to 1."""
    return [random.random() * 2 - 1 for _ in range(n)]


class Memento:
    def __init__(self, memory):
        self.__memory = memory

    @property
    def memory(self):
        return self.__memory

    @memory.deleter
    def memory(self):
        del self.__memory


class DumbNeuralNetwork():
    def __init__(self, weights_count):
        self.weights_count = weights_count
        self.weights = get_random_vector(self.weights_count)

    def train(self):
        random_vector = get_random_vector(self.weights_count)
        for i in range(self.weights_count):
            self.weights[i] += random_vector[i]

    def predict(self, X_test):
        return [
            sum(feature * coef for feature, coef in zip(x, self.weights))
            for x in X_test
        ]

    def evaluate(self, X_test, y_test):
        y_predicted = self.predict(X_test)
        loss_sum = sum(abs(y1 - y2) for y1, y2 in zip(y_predicted, y_test))
        loss_average = loss_sum / self.weights_count
        return loss_average

    def save_weights(self) -> Memento:
        """
        Save weights to restore them later.
        """
        return Memento(self.weights)

    def restore_weights(self, recollection: Memento):
        """
        Restore weights saved previously.
        """
        self.weights = recollection.memory


if __name__ == "__main__":
    saved_states: List[Memento] = []

    weights_count = 1000
    dumb_NN = DumbNeuralNetwork(weights_count)

    test_samples = 100
    # [[<float -1..1>, ...], ...]
    X_test = [get_random_vector(weights_count) for _ in range(test_samples)]
    # [<float -2000..2000>, ...]
    y_test = [value * weights_count * 2 for value in get_random_vector(test_samples)]

    epoch_number = 1000
    best_loss = weights_count * 2

    for epoch in range(epoch_number):
        dumb_NN.train()

        loss = dumb_NN.evaluate(X_test, y_test)
        print(f'{epoch}\t{loss}\t{best_loss}')

        if loss < best_loss:
            best_loss = loss
            saved_states.append(dumb_NN.save_weights())
        else:
            print(f'rolling back...')
            dumb_NN.restore_weights(saved_states[-1])
        clear_output(wait=True)
    print(f'Result: {best_loss}')

