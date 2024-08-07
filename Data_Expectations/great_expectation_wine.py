import pandas as pd
import json
import great_expectations as ge
from great_expectations.core.expectation_suite import ExpectationSuite

df = pd.read_csv(
    'C:/Users/ist.mevangelista/Documents/tcc/Datasets/wine/winequality-red.csv')

# Converta o DataFrame do pandas em um DataFrame do Great Expectations
df_ge = ge.from_pandas(df)

# Crie um novo conjunto de expectativas
suite = ExpectationSuite(expectation_suite_name="wine_expectations")

# Adicione suas expectativas
df_ge.expect_column_mean_to_be_between(
    'fixed acidity', min_value=4, max_value=16)
df_ge.expect_column_mean_to_be_between(
    'volatile acidity', min_value=0, max_value=2)
df_ge.expect_column_mean_to_be_between('citric acid', min_value=0, max_value=1)
df_ge.expect_column_mean_to_be_between(
    'residual sugar', min_value=0, max_value=15)
df_ge.expect_column_mean_to_be_between('chlorides', min_value=0, max_value=0.6)
df_ge.expect_column_mean_to_be_between(
    'free sulfur dioxide', min_value=0, max_value=72)
df_ge.expect_column_mean_to_be_between(
    'total sulfur dioxide', min_value=0, max_value=300)
df_ge.expect_column_mean_to_be_between(
    'density', min_value=0.990, max_value=1.005)
df_ge.expect_column_mean_to_be_between('pH', min_value=2.5, max_value=4)
df_ge.expect_column_mean_to_be_between('sulphates', min_value=0, max_value=2)
df_ge.expect_column_mean_to_be_between('alcohol', min_value=8, max_value=15)
df_ge.expect_column_values_to_be_in_set('quality', [3, 4, 5, 6, 7, 8])
for column in df.columns:
    df_ge.expect_column_values_to_not_be_null(column)
    df_ge.expect_column_values_to_be_in_type_list(
        column, ["int", "float", "string"])

# Adicione as expectativas à suite
suite.expectations = df_ge.get_expectation_suite(
    discard_failed_expectations=False)["expectations"]

# Salve o conjunto de expectativas
df_ge.save_expectation_suite("wine_expectations.json")

# Valide seu conjunto de dados em relação ao conjunto de expectativas
results = df_ge.validate(expectation_suite=suite)

# Converta o objeto de resultados em um dicionário
results_dict = results.to_json_dict()

# Salve os resultados em um arquivo JSON
with open('wine_results.json', 'w') as f:
    json.dump(results_dict, f)
