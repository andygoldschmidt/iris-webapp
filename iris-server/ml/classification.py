import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score


def classify(data, features, target):
    """
    Classifies the data and returns the confusion matrix and
    accuracy score.
    """
    df = pd.DataFrame(data)
    labels = df[target].unique()

    train, test = split_data(df)
    clf = train_model(train[features], train[target])
    predictions = predict(test[features], clf)

    cm = confusion_matrix(test[target], predictions)
    accuracy = accuracy_score(test[target], predictions)

    df_out = pd.DataFrame(cm, index=labels, columns=labels)
    return df_out.astype(float).to_dict(), accuracy


def train_model(data, target):
    rf = RandomForestClassifier()
    rf.fit(data, target)
    return rf


def predict(data, clf):
    return clf.predict(data)


def split_data(data, ratio_train=0.7):
    is_train = np.random.uniform(0, 1, len(data)) > ratio_train
    return data[is_train], data[-is_train]
