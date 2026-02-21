import os
import sys
import dill
import numpy as np
import pandas as pd

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException



def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for model_name, model in models.items():
            para = param[model_name]

           
            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

           
            best_model = gs.best_estimator_

            y_train_pred = best_model.predict(X_train)
            y_test_pred = best_model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            print(f"{model_name}")
            print("Best Parameters:", gs.best_params_)
            print("Training R2 Score:", train_model_score)
            print("Testing R2 Score:", test_model_score)
            print("=" * 50)

            
            report[model_name] = test_model_score

            
            models[model_name] = best_model

        return report

    except Exception as e:
        raise CustomException(e, sys)