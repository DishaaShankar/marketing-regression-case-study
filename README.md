# Marketing Channel Effectiveness and Sales Prediction

An end-to-end regression case study analyzing the relationship between advertising expenditure across TV, Radio, and Newspaper channels and product Sales using the ISLR Advertising dataset.

## Key Findings

- **Limited additional value from Newspaper:** Newspaper was statistically insignificant in the full additive model (p = 0.696). Removing it slightly improved 5-fold cross-validation RMSE from 1.676 to 1.648.
- **Nonlinear relationship and interaction effects:** Applying a square-root transformation to TV expenditure and introducing a TV–Radio interaction substantially improved predictive performance. Model D reduced cross-validation RMSE from 1.648 (Model B) to 0.474.
- **Statistical inference:** All three predictors in Model D remained statistically significant at p < 0.001 using HC3 robust standard errors. VIF values ranged from 1.002 to 1.007, indicating no concerning multicollinearity.
- **Held-out test performance:** Model D achieved an R² of 0.9945, RMSE of 0.4163, and MAE of 0.3503 on the untouched 40-observation test set.
- **Business scenario analysis:** Under a hypothetical fixed advertising budget of $150,000, the Radio-focused scenario produced the highest predicted Sales (16.96 thousand units), compared with 13.34 thousand units for the TV-focused scenario. These are exploratory predictions, not causal estimates or optimized budget recommendations.

## Model Comparison

**5-Fold Cross-Validation on Training Set (n = 160)**

| Model | Specification | Train R² | CV R² | CV RMSE | AIC |
|---|---|---:|---:|---:|---:|
| Model A | Full Additive (TV + Radio + Newspaper) | 0.896 | 0.870 | 1.676 | 621.284 |
| Model B | Reduced Additive (TV + Radio) | 0.896 | 0.874 | 1.648 | 619.442 |
| Model C | Linear Interaction (TV × Radio) | 0.966 | 0.959 | 0.942 | 443.809 |
| Model D | Nonlinear Interaction (√TV × Radio) | 0.992 | 0.990 | 0.474 | 206.744 |

## Project Structure

```text
Marketing Spend vs Revenue Analysis/
│
├── Dataset/
│   └── Advertising.csv
│
├── Notebooks/
│   ├── 1_data_understanding.ipynb
│   ├── 2_eda.ipynb
│   ├── 3_simple_linear_regression.ipynb
│   ├── 4_multiple_linear_regression.ipynb
│   ├── 5_statistical_testing.ipynb
│   └── 6_model_diagnostics.ipynb
│
├── src/
│   ├── __init__.py
│   └── utils.py
│
├── reports/
│   └── final_report.md
│
├── requirements.txt
└── README.md
```

## Methodology

1. Data understanding and quality checks
2. Exploratory Data Analysis (EDA)
3. Simple Linear Regression
4. Multiple Linear Regression
5. Feature engineering and interaction analysis
6. Five-fold cross-validation and model comparison
7. Statistical testing and multicollinearity analysis
8. Regression diagnostics and influential observation analysis
9. Final evaluation on the held-out test dataset
10. Hypothetical business scenario analysis

## Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Statsmodels
- Jupyter Notebook

## How to Run

1. Clone this repository.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Open the project in Jupyter Notebook or VS Code.
4. Run notebooks 1 through 6 in sequence.

## Dataset

The project uses the Advertising dataset from *An Introduction to Statistical Learning (ISLR)*.

Source: [ISLR – Advertising Dataset](https://www.statlearning.com/resources-first-edition)

The dataset contains 200 observations with advertising expenditure across TV, Radio, and Newspaper channels and corresponding Sales.

## Limitations

- The dataset contains only 200 observations, with 40 reserved for final testing.
- The analysis uses observational data and cannot establish causal relationships between advertising expenditure and Sales.
- The selected model uses TV and Radio expenditure; Newspaper is excluded.
- Residual diagnostics identified non-normality and heteroscedasticity.
- Hypothetical budget scenarios require further validation using real-world campaign data.
- Model performance should be evaluated on larger, independent datasets before practical deployment.
