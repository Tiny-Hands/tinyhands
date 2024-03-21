import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from datetime import date
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from time import time
from .case_dispatcher_logging import setup_logger
from pathlib import Path
import pickle
from datetime import datetime
from sklearn.preprocessing import FunctionTransformer


logger = setup_logger("model_logging", "model")


class TypeSelector(BaseEstimator, TransformerMixin):
    """
    A transformer for selecting columns based on data type.

    Parameters
    ----------
    dtype : str or list-like of str
        The data type(s) to include.

    Attributes
    ----------
    dtype : str or list-like of str
        The data type(s) to include.

    Methods
    -------
    fit :
        No operation is performed.
    transform :
        Selects columns of the input data frame that have the specified data type(s).

    Example
    -------
    >>> selector = TypeSelector("float64")
    >>> X = pd.DataFrame({"col1": [1, 2, 3], "col2": [0.1, 0.2, 0.3]})
    >>> selector.transform(X)
       col2
    0  0.1
    1  0.2
    2  0.3
    """

    def __init__(self, dtype):
        self.dtype = dtype

    def fit(self, X, y=None):
        """No operation is performed."""
        return self

    def transform(self, X):
        """
        Selects columns of the input data frame that have the specified data type(s).

        Parameters
        ----------
        X : pd.DataFrame
            The input data frame.

        Returns
        -------
        X_selected : pd.DataFrame
            The selected columns of the input data frame.
        """
        assert isinstance(X, pd.DataFrame)
        return X.select_dtypes(include=[self.dtype])


def save_results(best_model, X_validation):
    """Pickles model and column names and saves them for later use with a timestamp."""

    # Get current date and time

    datetime_now = datetime.now()
    # Format the date and time in a string (e.g., '2023_12_07_15_30')
    timestamp = datetime_now.strftime("%Y_%m_%d_%H_%M")

    # Append timestamp to filenames
    model_filename = f"models/u21_rf_model_{timestamp}.sav"
    xcols_filename = f"model_compare_data/xcols_{timestamp}.txt"

    # Save the model
    pickle.dump(best_model, open(model_filename, "wb"))

    # Save the column names
    xcols = list(X_validation.columns)
    with open(xcols_filename, "w") as f:
        for item in xcols:
            f.write("%s\n" % item)


# You can then call this function with your model and validation data
# save_results(your_model, your_validation_data)
def build_transformer():
    """
    Builds a transformer that applies a no-operation (identity function) to the data,
    preserving both the data and column order exactly as is.
    """
    # No-op transformer for the entire DataFrame
    no_op_transformer = FunctionTransformer()

    # Wrap the no-op transformer in a pipeline (optional, depending on further needs)
    transformer = Pipeline([
        ("no_op", no_op_transformer),
    ])

    return transformer

def build_transformer_depr():
    """
    Builds a transformer for processing data without altering the original types of boolean and integer columns.
    """
    transformer = Pipeline([
        ("features", FeatureUnion(
            transformer_list=[
                ("boolean",
                    Pipeline([
                        ("selector", TypeSelector("bool")),
                        # Potentially add steps if needed, but none are needed now
                    ])
                ),
                ("integers",
                    Pipeline([
                        ("selector", TypeSelector('int')),
                        # No scaling or further steps for integers
                    ])
                ),
                # Add a branch for floats if any specific processing is required for float columns
            ],
            n_jobs=1,
        )),
    ])

    return transformer



def remove_recent(soc_df, cutoff_days):
    """
    Eliminates cases more recent than the cutoff date.

    Parameters:
        soc_df (pandas.DataFrame): A dataframe containing case information.
        cutoff_days (int): The number of days from the present to use as the cutoff point.

    Returns:
        pandas.DataFrame: A dataframe containing only cases that are older than the cutoff date or that resulted in an arrest.
    """
    # Get the current date and format it as a string
    today = date.today()
    today.strftime("%m/%d/%Y")

    # Calculate the number of days between today and the interview date for each case
    # df['Days'] = (today - df.loc[:, 'interview_date']) / np.timedelta64(1, 'D')
    today = pd.Timestamp(today)

    soc_df["interview_date"] = pd.to_datetime(soc_df["interview_date"])
    soc_df["Days"] = (today - soc_df.loc[:, "interview_date"]).dt.days

    # Create a new dataframe containing only cases that are older than the cutoff date or that resulted in an arrest
    sub_df = soc_df[(soc_df["Days"] > cutoff_days) | (soc_df["arrested"] == 1)]

    return sub_df


def train_test_val_split(sub_df, te_size=0.2, val_size=0.1):
    """
    Splits dataset into training, testing, and validation sets.

    Parameters
    ----------
    sub_df : DataFrame
        The input DataFrame to split.
    te_size : float, optional
        The size of the test set, as a fraction of the input data. The default is 0.2.
    val_size : float, optional
        The size of the validation set, as a fraction of the training set. The default is 0.1.

    Returns
    -------
    tuple
        Four DataFrames, representing the training, validation, and testing sets.
    """
    # Save the 'Arrest' column as y
    sub_df.to_csv(Path("data/modelbuild_sub_df.csv"))
    y = sub_df.arrested

    # Remove certain columns from the DataFrame, except 'Arrest'
    X = sub_df.drop(
        columns=[
            "arrested",
            "sf_number",
            "Days",
            "interview_date",
            "suspect_id",
            "person_id",
            "case_notes",
            "social_media",
            "master_person_id",
            "operating_country_id",
            "country",
            "sf_number_group",
        ]
    )

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=te_size)

    # Calculate the validation set size as a fraction of the training set
    val_size = val_size / (1 - te_size)

    # Split the training set into training and validation sets
    X_train, X_validation, y_train, y_validation = train_test_split(
        X_train, y_train, test_size=val_size
    )

    # Return the training, validation, and testing sets
    return X_train, X_validation, y_train, y_validation


def get_cls_pipe(clf=RandomForestClassifier()):
    """
    Builds a pipeline with a transformer and a classifier algorithm.

    Args:
        clf (object, optional): The classifier algorithm to use in the pipeline. Defaults to a RandomForestClassifier.

    Returns:
        object: A pipeline with a transformer and classifier.
    """
    # Build the transformer
    transformer = build_transformer()

    # Create the pipeline with the transformer and classifier
    cls_pipeline = Pipeline([("transformer", transformer), ("clf", clf)])
    logger.info(f"Case Dispatcher 6.0: Built cls pipeline")

    # Return the pipeline
    return cls_pipeline



def pipe_predict(cls_pipeline, X_train, y_train, X_validation):
    """Make predictions with classifier pipeline."""
    cls_pipeline.fit(X_train, y_train)
    y_rf = cls_pipeline.predict_proba(X_validation)
    return y_rf


def do_gridsearch(cls_pipeline, X_train, y_train):
    """
    Conduct grid search cross-validation on a classifier pipeline to find the best model.

    Args:
        cls_pipeline: A scikit-learn pipeline object containing a classifier.
        X_train (array-like): Training data.
        y_train (array-like): Training labels.

    Returns:
        sklearn.model_selection._search.GridSearchCV: The best model found by grid search.
    """
    # Define the parameter grid for the grid search
    search_space = [
        {
            "clf": [RandomForestClassifier()],
            "clf__bootstrap": [False, True],
            "clf__n_estimators": [10, 100],
            #'clf__max_depth': [5, 10, 20, 30, 40, 50, None],
            "clf__max_depth": [20, 30],
            #'clf__max_features': [0.5, 0.6, 0.7, 0.8, 1],
            "clf__max_features": [0.5, 0.6],
            "clf__class_weight": ["balanced", None],
        }
    ]
    #'clf__class_weight': ["balanced",
    #                      "balanced_subsample", None]}]
    logger.info(f"Case Dispatcher 3.0: Start grid search")
    # Create a grid search object using the classifier pipeline and parameter grid
    grid_search = GridSearchCV(cls_pipeline, search_space, cv=4, n_jobs=-1, verbose=1)
    logger.info(f"Case Dispatcher 3.0: Completed grid search")
    # Print the parameters being searched
    print("Performing grid search...")
    print("parameters:")
    print(search_space)

    # Start the timer and conduct the grid search
    t0 = time()
    best_model = grid_search.fit(X_train, y_train)
    print("done in %0.3fs" % (time() - t0))
    print()

    # Get the best parameters from the model
    best_parameters = best_model.best_estimator_.get_params()["clf"]

    # Print the best score and parameters found by the grid search
    print("Best score: %0.3f" % grid_search.best_score_)
    print("Best parameters set:")
    print(best_parameters)

    # Return the best model
    return best_model


def full_gridsearch_pipe(soc_df, cutoff_days=90):
    sub_df = remove_recent(soc_df, cutoff_days)
    X_train, X_validation, y_train, y_validation = train_test_val_split(sub_df)
    X_train.to_csv("data/case_dispatcher_X_train.csv", index=False)
    y_train.to_csv("data/case_dispatcher_y_train.csv", index=False)
    X_validation.to_csv("data/case_dispatcher_X_validation.csv", index=False)
    y_validation.to_csv("data/case_dispatcher_y_validation.csv", index=False)
    cls_pipeline = get_cls_pipe()
    best_model = do_gridsearch(cls_pipeline, X_train, y_train)
    x_cols = list(X_validation.columns)
    return best_model, x_cols, X_validation


def check_grid_search_cv(soc_df, gscv, cutoff_days):
    """Check to see if Grid Search CV is on, and if it is run Grid Search CV."""
    if gscv == "On":
        best_model, x_cols, X_Validation = full_gridsearch_pipe(soc_df, cutoff_days)
    return best_model, x_cols, X_Validation


def make_new_predictions(df, soc_model, x_cols):
    """Use existing classifier algorithm on new cases without recalculating
    best fit."""
    X = df[df.columns.intersection(x_cols)]
    df["soc"] = soc_model.predict_proba(X)[:, 1]
    return df


def load_model(dir_name, file_prefix):
    model_filename = f"{dir_name}/{file_prefix}_model.sav"
    loaded_model = pickle.load(open(model_filename, "rb"))
    return loaded_model
