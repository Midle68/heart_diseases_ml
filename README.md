# The project: Prediction of a heart disease 

## Description of the project

The goal of the project is to predict heart diseases based on the given data. The target variable is **'cardio'**. The evalution metric for the project is **ROC-AUC**.

The given dataset gives the following parameters of the objects:
- id;
- age;
- gender;
- height;
- weight;
- ap_hi;
- ap_lo;
- cholesterol;
- gluc;
- smoke;
- alco;
- active.

## Plan of the project:
1. Import of Modules & Files Opening
2. Data Preprocessing and Exploratory Data Analysis (EDA)
3. Development of ML-models
4. Conclusion

## Fulfilled tasks:
1. Created a ML-model (**RandomForestClassifier**) for the regression task, which determines the presence of a heart diseases. **ROC-AUC** of the model: 0.739. The hyperparameters of the model are the following: **criterion = 'entropy', n_estimators = 350, max_depth = 10**.
2. Created a web-application using which a person can find the risk of a heart disease (that's a model. In case of anything, refer to a specialist).

## Used libraries:

`matplotlib`, `numpy`. `pandas`, `phik`, `pickle`, `seaborn`, `sklearn`
