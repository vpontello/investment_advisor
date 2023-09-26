# Investment Advisor

## Blogpost

To understand better the motivation and the project as a whole, pleas check the [blogbost](https://medium.com/@ing.victorpontello/unleashing-ais-power-transforming-investments-with-data-and-analytics-6a06730ed779) with all the findings and important information about the project.

## Description

This project utilizes stock data from the Brazilian market and macroeconomic data to predict the stock with higher probability of getting the best dividend yield. Dividend yield is a financial ratio that shows the percentage return an investor can expect from a company's dividend payments relative to its stock price.

## Problem Statement and Motivation

Predicting stocks that generate the best dividend yield is a complex task that requires extensive research and analysis. The manual approach is time-consuming and prone to human error. By leveraging machine learning, we can create predictive models that analyze historical stock data and macroeconomic indicators to identify high-yield dividend stocks. This data-driven approach saves time, enhances decision-making, and increases the chances of making profitable investments in the stock market.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Methodology](#methodology)
- [Results](#results)
- [Future Work](#future-work)
- [License](#license)

## Installation

To use this project, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/project-name.git`.
2. Make sure to have all the packages from the `requirements.txt` installed.
3. Navigate to the project directory: `cd project-name`.
4. Navigate through the notebooks in the folder `notebooks`.


## Usage

1. Run notebook `00_data_eng.ipynb` to extract transform and load the raw data.
2. Run notebook `01_data_prep.ipynb` to generate the base datasets.
3. Run notebook `02_ml_pipeline.ipynb` to create the ML pipeline and train the models.
4. Run notebook `03_data_analysis.ipynb` to analyse the results.

## Data Sources

The data used in this project is stored in a GCP Clud Sorage bucket called `storage barsianize`.
This bucket is enabled for reading purposes.

All the extraction, transformation and loading of the data is performed and documented in the `00_data_eng.ipynb` notebook.

## Methodology

The methodology for predicting the best dividend yield involves both `LightGBM` and `XGBoost` regressors. Here are the main steps:

1. **Data preprocessing:** After gathering all raw data, some feature engineering is performed, and the base dataset is created.

2. **Feature selection:** The feature selection processes goes along through 3 steps. firstly the XGBoost model and the LightGBM model are trained and the feature importance calculated. After that, another LightGBM model is trained with the most important features from both. After that the feature importance is calculated again and the most important are selected. All the models are taken into account by making recommendations. The performance of each of them is the definitive factor to choose the model

3. **Model training:**
 In the whole process a 5-Fold-CV is performed and is based on the results, that the model is evaluated. All the training process is performed inside a pipeline, to avoid both data leakege and to guarantee, for example that the output is linked to the right preprocessing technique, such as Standardization or Normalization. The hyperparameter tunning is perrformed in a series of grid seaches, to assure that the best configuration is used.

4. **Model evaluation:**

    For the model evaluation the following metrics were used:
    **R2, MSE, explained_variance_score,** and **MAPE** 

    Which are valuable metrics for evaluating the model's performance in predicting the best dividend yield.

    * **R2** measures how well the model predicts the dividend yield by explaining the variance in the dependent variable.
    * **MSE** quantifies the average squared difference between predicted and actual dividend yield, indicating overall accuracy.
    * **explained_variance_score**: shows the proportion of variance in actual dividend yield explained by the model.
    * **MAPE** calculates the average percentage difference between predicted and actual dividend yield, providing insight into prediction errors.

    Using these metrics helps assess the model's accuracy, predictive power, and the magnitude of prediction errors, aiding in decision-making and model refinement.

## Results

The results of the prediction model are:
 * `Best Parameters`: "reg__learning_rate": 0.1, "reg__n_estimators": 500, reg__reg_alpha": 0.1, "reg__reg_lambda": 0.01, "reg__learning_rate": 0.5, "reg__max_depth": 5, "reg__n_estimators": 1000, "reg__reg_alpha": 0.1, "reg__reg_lambda": 0.01
 * `Performance`: 
    * `Cross Validation Scores`: 
        * `test_r2`: [0.9026566281152357, 0.9551451566422728, 0.9219706170152273, 0.8742180629048635, 0.9275396568707293], 
        * `test_mse`: [0.0002454358206710687, 0.00012158997391454887, 0.00020362955465438526, 0.000337151021024389, 0.00021951336658258087], 
        * `test_xve`: [0.9026619283913273, 0.955149523900871, 0.9219706230473486, 0.8742180890863059, 0.9275502032567448], 
        * `test_MAPE`: [4152855564939.0933, 2877504178625.054, 2852303507918.8237, 4493613707946.239, 2811455750330.8335]. 

## Future Work

For further develop the project, I foresee an automation to collect the daily data from the source, minimizing the necessity of interpolation between the days, what is big source of inefficiency of the model. Furthermore, more possibilities related to feature engineering can be explored, specially based on the finance literature.

## License

MIT License
