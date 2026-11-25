# Marketing Channel Effectiveness and Sales Prediction Using Linear Regression

## 1. Executive Summary

This project analyzes the relationship between advertising expenditure across three marketing channels — TV, Radio, and Newspaper — and product Sales.

The primary objective was to identify which advertising channels have stronger relationships with Sales, investigate whether combining channels improves predictive performance, and develop a regression model to predict Sales based on advertising expenditure.

Exploratory Data Analysis revealed that TV and Radio had stronger individual relationships with Sales than Newspaper. Multiple regression models were developed and compared using 5-fold cross-validation.

The selected model incorporated a square-root transformation of TV expenditure and a TV–Radio interaction term. It achieved an R² of **0.9945**, an MAE of **0.3503**, and an RMSE of **0.4163** on the held-out test dataset.

The analysis also included statistical testing, model diagnostics, and hypothetical advertising budget scenarios to explore the model's business applications.

Overall, the project demonstrates a structured regression workflow, from data exploration and model development to evaluation and business interpretation. Since the dataset is observational, the identified relationships should not be interpreted as proof of causal advertising impact.

## 2. Business Problem and Objectives

### Business Problem

Businesses invest in multiple advertising channels, but understanding how expenditure across these channels relates to Sales is essential for making informed marketing decisions.

The objective of this analysis is to examine the relationship between advertising expenditure on TV, Radio, and Newspaper and product Sales, identify which channels provide stronger predictive information, and understand whether combining advertising channels improves Sales prediction.

### Project Objectives

1. Analyze the relationship between advertising expenditure across TV, Radio, and Newspaper and product Sales.
2. Identify the advertising channels with stronger individual relationships with Sales.
3. Investigate potential nonlinear relationships and interaction effects between advertising channels.
4. Develop and compare multiple linear regression models using cross-validation.
5. Evaluate the statistical significance of model predictors and assess regression assumptions.
6. Evaluate the final model on an untouched test dataset.
7. Explore hypothetical advertising budget allocation scenarios to understand their predicted Sales outcomes.

### Expected Outcome

Develop a reliable regression model that predicts Sales based on advertising expenditure and provides analytical insights that can support marketing budget discussions.

The analysis is intended to identify associations and predictive patterns, rather than establish causal advertising effectiveness or determine an optimal budget allocation.

## 3. Dataset Description

### Data Source

The project uses the Advertising dataset from the textbook *An Introduction to Statistical Learning (ISLR)*.

Source: [ISLR – Advertising Dataset](https://www.statlearning.com/resources-first-edition)

### Dataset Overview

The dataset contains **200 observations** representing advertising expenditure across three marketing channels and the corresponding product Sales.

| Variable | Description | Measurement Unit |
|---|---|---|
| TV | Advertising expenditure on TV | Thousands of dollars |
| Radio | Advertising expenditure on Radio | Thousands of dollars |
| Newspaper | Advertising expenditure on Newspaper | Thousands of dollars |
| Sales | Product Sales | Thousands of units |

### Dataset Characteristics

- Total observations: 200
- Independent variables: 3 (TV, Radio, Newspaper)
- Target variable: Sales
- Data type: Numerical
- Missing values: None
- Duplicate records: None

### Data Preparation

The dataset was loaded using Pandas, and the unnecessary index column was excluded during import.

The data was divided into training and testing sets using an 80:20 split with `random_state=42`.

- Training set: 160 observations
- Testing set: 40 observations

The training dataset was used for exploratory analysis, model development, cross-validation, and statistical testing. The test dataset was kept separate and used only for the final model evaluation.

## 4. Data Cleaning and Preparation

Before performing exploratory data analysis, the dataset was checked for data quality and consistency.

### Data Quality Checks

The following checks were performed:

- **Missing Values:** No missing values were found in the dataset.
- **Duplicate Records:** No duplicate observations were identified.
- **Data Types:** All four variables were numerical (`float64`).
- **Column Names:** Column names were converted to lowercase for consistency.
- **Unnecessary Columns:** The original dataset index column was excluded during import.

### Outlier Investigation

The Interquartile Range (IQR) method was used to identify potential outliers in the numerical variables.

Newspaper expenditure contained a potential upper outlier. Further inspection showed that the observation had valid advertising expenditure and Sales values.

Therefore, the observation was retained rather than removed solely based on the statistical outlier threshold.

Cook's Distance was later used during model diagnostics to investigate potentially influential observations.

### Train-Test Separation

The dataset was split into training and testing sets using an 80:20 ratio.

All exploratory analysis and model development were performed using the training dataset. The test dataset was reserved for final evaluation to reduce the risk of data leakage.

## 5. Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed on the training dataset to understand variable distributions, identify potential outliers, and examine relationships between advertising expenditure and Sales.

### 5.1 Descriptive Statistics

The descriptive statistics provided an overview of the distribution and variability of each variable.

| Variable | Mean | Median | Standard Deviation | Skewness |
|---|---:|---:|---:|---:|
| TV | 150.019 | 150.65 | 84.419 | -0.094 |
| Radio | 22.876 | 21.20 | 14.805 | 0.132 |
| Newspaper | 29.946 | 25.60 | 20.336 | 0.707 |
| Sales | 14.100 | 13.20 | 5.109 | 0.405 |

TV expenditure showed a nearly symmetric distribution, while Newspaper expenditure exhibited moderate positive skewness.

### 5.2 Relationship Between Advertising Channels and Sales

Pearson correlation was used to examine the strength and direction of linear relationships between the variables.

| Variable | Correlation with Sales |
|---|---:|
| TV | 0.769 |
| Radio | 0.592 |
| Newspaper | 0.238 |

Key observations:

- TV expenditure showed the strongest positive correlation with Sales.
- Radio expenditure also demonstrated a moderately strong positive correlation with Sales.
- Newspaper expenditure showed a comparatively weak positive correlation with Sales.

These findings suggest that TV and Radio provide stronger individual predictive information about Sales than Newspaper.

### 5.3 Outlier Analysis

The IQR method identified a potential upper outlier in Newspaper expenditure. The observation was retained because its values appeared valid and there was no sufficient evidence to classify it as an erroneous record.

### 5.4 Key EDA Findings

The exploratory analysis indicated that TV and Radio were more strongly associated with Sales than Newspaper. These findings informed the subsequent regression analysis, where individual channel models and multiple regression models were evaluated.

The observed correlations represent associations and do not establish causal relationships between advertising expenditure and Sales.

## 6. Modeling Approach and Model Comparison

### 6.1 Simple Linear Regression

Three separate simple linear regression models were developed to evaluate the individual relationship between each advertising channel and Sales.

| Advertising Channel | Training R² | Training RMSE | Training MAE |
|---|---:|---:|---:|
| TV | 0.591 | 3.256 | 2.583 |
| Radio | 0.351 | 4.103 | 3.143 |
| Newspaper | 0.057 | 4.947 | 3.998 |

TV provided the strongest individual predictive performance, followed by Radio. Newspaper had the weakest individual predictive performance.

### 6.2 Multiple Linear Regression

Four multiple regression models were developed to investigate whether combining advertising channels, introducing interaction effects, and applying nonlinear transformations could improve predictive performance.

| Model | Features | Description |
|---|---|---|
| Model A | TV + Radio + Newspaper | Full additive model |
| Model B | TV + Radio | Reduced additive model |
| Model C | TV + Radio + TV × Radio | Linear interaction model |
| Model D | √TV + Radio + √TV × Radio | Nonlinear interaction model |

### 6.3 Model Comparison Using Cross-Validation

Five-fold cross-validation was performed using the training dataset to compare model performance.

| Model | Training R² | Training RMSE | CV R² | CV RMSE |
|---|---:|---:|---:|---:|
| Model A | 0.896 | 1.645 | 0.870 | 1.676 |
| Model B | 0.896 | 1.646 | 0.874 | 1.648 |
| Model C | 0.966 | 0.945 | 0.959 | 0.942 |
| Model D | 0.992 | 0.450 | 0.990 | 0.474 |

### 6.4 Model Selection

Model D, incorporating a square-root transformation of TV expenditure and a TV–Radio interaction term, achieved the best cross-validation performance among the four models.

It obtained a cross-validation R² of **0.990** and an RMSE of **0.474**, indicating substantially better predictive performance than the other evaluated models.

Based on these results, Model D was selected as the final candidate for statistical testing, diagnostic analysis, and evaluation on the held-out test dataset.

## 7. Statistical Testing and Model Diagnostics

The selected Model D was further examined using statistical tests and regression diagnostics to assess predictor significance, multicollinearity, and potential violations of regression assumptions.

### 7.1 Statistical Significance of Predictors

An Ordinary Least Squares (OLS) regression model was fitted using the training dataset.

The overall model was statistically significant, with an F-statistic of approximately 6,600 and a p-value below 0.001.

All three model terms were statistically significant:

| Predictor | Coefficient | p-value |
|---|---:|---:|
| √TV (centered) | 0.9352 | < 0.001 |
| Radio (centered) | 0.1982 | < 0.001 |
| TV–Radio Interaction | 0.0214 | < 0.001 |

The positive interaction coefficient indicates that the association between transformed TV expenditure and Sales becomes stronger at higher Radio expenditure, and vice versa.

These coefficients represent conditional associations and should not be interpreted as causal advertising effects.

### 7.2 Multicollinearity Analysis

Variance Inflation Factor (VIF) was calculated to assess multicollinearity among the model predictors.

| Predictor | VIF |
|---|---:|
| √TV (centered) | 1.007 |
| Radio (centered) | 1.002 |
| Interaction | 1.007 |

All VIF values were close to 1, indicating no concerning multicollinearity among the predictors.

### 7.3 Robust Standard Errors

HC3 heteroscedasticity-robust standard errors were calculated to make statistical inference more robust to potential heteroscedasticity.

The predictor coefficients remained unchanged, and all three model terms remained statistically significant.

### 7.4 Interaction Significance Test

A nested model F-test was performed to compare the additive model against the interaction model.

- F-statistic: 1329.665
- p-value: 3.0362 × 10⁻⁷⁸

The result indicates that adding the interaction term significantly improved model fit compared with the additive model.

### 7.5 Residual Diagnostics

The following diagnostic tests were performed:

**Shapiro-Wilk Test**

- Test statistic: 0.9523
- p-value: 0.0000287

The test rejected the null hypothesis of normally distributed residuals, indicating a statistically significant deviation from normality.

**Breusch-Pagan Test**

- LM statistic: 25.2743
- p-value: 0.0000135

The test rejected the null hypothesis of constant error variance, indicating evidence of heteroscedasticity.

HC3 robust standard errors were used to improve the reliability of coefficient inference under heteroscedasticity. However, they do not eliminate the underlying variance pattern.

### 7.6 Influential Observations – Cook's Distance

Cook's Distance was used to identify observations that could have a substantial influence on the fitted regression model.

Using the threshold of 4/n, where n = 160, the cutoff was 0.025.

A total of 12 observations exceeded this threshold. The highest Cook's Distance values were:

| Original Observation Index | Cook's Distance |
|---:|---:|
| 131 | 0.5726 |
| 156 | 0.3654 |
| 3 | 0.2038 |

These observations were flagged for further attention. They were not automatically removed because a high Cook's Distance does not necessarily indicate an erroneous observation.

### 7.7 Diagnostic Summary

The selected model demonstrated statistically significant predictors and no concerning multicollinearity. However, the residual tests indicated non-normality and heteroscedasticity.

These findings were considered when interpreting the model's statistical results and predictive performance.

## 8. Final Model Evaluation

After completing model selection and diagnostic analysis, the selected regression model was evaluated on the previously untouched test dataset containing 40 observations.

The final model was fitted using the complete training dataset, and the same feature transformations and training-set means were applied to the test dataset.

### Test Set Performance

| Evaluation Metric | Test Result |
|---|---:|
| R² | 0.9945 |
| MAE | 0.3503 |
| RMSE | 0.4163 |

### Performance Interpretation

- **R² (0.9945):** The model explains approximately 99.45% of the variation in Sales within the test dataset.
- **MAE (0.3503):** The average absolute prediction error is approximately 0.3503 thousand units, equivalent to around 350 units.
- **RMSE (0.4163):** The root mean squared prediction error is approximately 0.4163 thousand units, equivalent to around 416 units.

### Cross-Validation vs Test Performance

The final test performance was consistent with the earlier cross-validation results.

| Metric | Cross-Validation | Test Dataset |
|---|---:|---:|
| R² | 0.990 | 0.9945 |
| RMSE | 0.474 | 0.4163 |

The model maintained strong predictive performance on the held-out observations, with no noticeable deterioration compared with cross-validation.

These results are encouraging, but the test dataset contains only 40 observations. Further validation on larger and independent datasets would be necessary to assess performance in other business environments.

## 9. Business Scenario Analysis

To explore how different advertising budget allocations relate to predicted Sales, three hypothetical budget strategies were evaluated using the selected regression model.

A fixed total advertising budget of $150,000 was considered across TV and Radio.

### 9.1 Scenario Comparison

| Strategy | TV Budget ($000s) | Radio Budget ($000s) | Predicted Sales (000s) |
|---|---:|---:|---:|
| TV-focused | 130 | 20 | 13.34 |
| Balanced | 110 | 40 | 16.04 |
| Radio-focused | 101 | 49 | 16.96 |

### 9.2 Key Observations

- The TV-focused strategy produced the lowest predicted Sales of 13.34 thousand units.
- The Balanced strategy produced predicted Sales of 16.04 thousand units.
- The Radio-focused strategy produced the highest predicted Sales of 16.96 thousand units among the three scenarios.

The Radio-focused strategy showed approximately 3.62 thousand more predicted units in Sales than the TV-focused strategy.

### 9.3 Business Interpretation

For the hypothetical budget allocations evaluated, the model predicted higher Sales for strategies involving greater Radio expenditure.

This suggests that allocations with relatively higher Radio spending are associated with higher predicted Sales under the fitted model.

However, these scenarios are exploratory predictions based on historical observational data. They do not establish that reallocating advertising expenditure towards Radio will directly cause Sales to increase.

The analysis also considers only TV and Radio expenditure, as Newspaper was not included in the selected model. These scenarios should therefore not be treated as optimal budget recommendations without further validation using real-world campaign data.

## 10. Key Findings and Business Recommendations

### Key Findings

1. **TV and Radio showed stronger individual relationships with Sales:** TV had the highest individual correlation with Sales (0.769), followed by Radio (0.592). Newspaper showed a weaker correlation (0.238).

2. **Interaction effects improved predictive performance:** The model incorporating a square-root transformation of TV expenditure and a TV–Radio interaction achieved the best cross-validation performance among the evaluated models.

3. **Strong test-set performance:** The selected model achieved an R² of 0.9945 and an RMSE of 0.4163 on the held-out test dataset.

4. **Statistical diagnostics identified limitations:** The residual tests indicated non-normality and heteroscedasticity, while VIF values showed no concerning multicollinearity.

5. **Radio-focused scenario had the highest predicted Sales:** Among the three hypothetical budget allocations, the Radio-focused strategy produced the highest predicted Sales of 16.96 thousand units.

### Business Implications

- TV and Radio expenditure may deserve closer attention in marketing performance analysis because they showed stronger relationships with Sales in this dataset.
- The interaction between TV and Radio suggests that evaluating advertising channels together may provide more useful predictive insights than examining them independently.
- The scenario analysis can support discussions about alternative advertising budget allocations.
- Before implementing budget changes, businesses should validate these findings using actual campaign results and controlled experiments where feasible.

These findings provide analytical insights to support marketing discussions, but they do not establish causal advertising effectiveness or identify an optimal budget allocation.

## 11. Limitations

Despite the strong predictive performance, this analysis has several limitations:

1. **Limited Dataset Size:** The dataset contains only 200 observations, with 160 used for training and 40 for testing. This limits the amount of data available for model development and evaluation.

2. **Observational Data:** The dataset captures historical advertising expenditure and Sales. Therefore, the relationships identified cannot establish that changes in advertising expenditure directly cause changes in Sales.

3. **Limited Predictors:** The analysis considers only TV, Radio, and Newspaper expenditure. Other factors, such as product pricing, promotions, competition, seasonality, and market conditions, are not included.

4. **Model Assumptions:** Diagnostic tests identified non-normal residuals and heteroscedasticity. Although HC3 robust standard errors were used for statistical inference, these issues remain relevant when interpreting the model.

5. **Limited Generalizability:** The dataset may not represent current advertising environments or other businesses. Further validation on larger and independent datasets is required.

6. **Exploratory Business Scenarios:** The hypothetical budget scenarios are model-based predictions, not experimentally validated outcomes or optimized budget recommendations.

## 12. Conclusion

This project investigated the relationship between advertising expenditure across TV, Radio, and Newspaper channels and product Sales using regression analysis.

Through exploratory data analysis, simple and multiple linear regression, cross-validation, statistical testing, and model diagnostics, the project identified TV and Radio as stronger individual predictors of Sales than Newspaper.

Among the four multiple regression models evaluated, the model incorporating a square-root transformation of TV expenditure and a TV–Radio interaction achieved the best cross-validation performance.

The selected model achieved an R² of **0.9945**, an MAE of **0.3503**, and an RMSE of **0.4163** on the held-out test dataset.

The business scenario analysis further demonstrated how the fitted model can be used to explore hypothetical advertising budget allocations and compare their predicted Sales outcomes.

Overall, this project demonstrates an end-to-end regression analysis workflow, from data preparation and exploratory analysis to model development, statistical evaluation, and business interpretation. It also highlights the importance of understanding model limitations and distinguishing predictive relationships from causal conclusions.

