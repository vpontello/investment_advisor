# Investment Advisor

## Backlog
* finish documentation
* split ingestion code into a script
* generate requirements.txt
* create EDA notebook
* split the training pipeline into a script
* add a simulation of the top 10 companies based on the actual data
* generate predicions with the data from last year and compare with the actual best results
* compare with the list of the biggest companies from last year
* implement a backtest simulating the last 10 years using this strategy and just using the great 10.
* implement SHAP values.
* create possible developments to the project
    * deep dive into the feature selection
    * test more algorithms 
* write the blog post


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
- [Contributing](#contributing)
- [License](#license)

## Installation

To use this project, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/project-name.git`
2. Navigate to the project directory: `cd project-name`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Make sure you have installed all the dependencies (see Installation section).
2. Obtain the necessary stock data and macroeconomic data from the specified sources (see Data Sources section).
3. Place the data files in the appropriate directories within the project.
4. Run the main script: `python main.py`
5. Follow the prompts and input the required information when prompted.
6. The script will generate the predicted dividend yields based on the provided data.

## Data Sources

This project utilizes the following data sources:

- Stock data: Data for the Brazilian market can be obtained from [source_name].
- Macroeconomic data: [Description of the source and how to obtain the data]

Please ensure that you have the necessary permissions and licenses to use the data from these sources.

## Methodology

The methodology for predicting the best dividend yield involves [describe the approach or algorithm used]. Here are the main steps:

1. **Data preprocessing:** [Describe how the data is prepared for analysis]

2. **Feature selection:** [Explain the criteria used for selecting relevant features]

3. **Model training:**
 [Describe the model used for prediction and how it is trained]

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

The results of the prediction model are [describe the outcomes, such as accuracy, performance metrics, or any other relevant information]. 

## Future Work

There are several areas of improvement and future work for this project, including:

- [List potential enhancements or additions to the project]
- [Suggest ways to expand the scope or incorporate additional features]

Contributions from the open-source community are welcome to further improve the project.

## Contributing

If you want to contribute to this project, follow the steps below:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit them: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request.

## License

[Specify the license under which the project is released. For example: MIT License, Apache License, etc.]
