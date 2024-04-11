import pandas as pd
import json
import great_expectations as ge
from great_expectations.core.expectation_suite import ExpectationSuite

df = pd.read_csv('diabetes.csv')

# Converta o DataFrame do pandas em um DataFrame do Great Expectations
df_ge = ge.from_pandas(df)

# Crie um novo conjunto de expectativas
suite = ExpectationSuite(expectation_suite_name="diabetes_expectations")

# Adicione suas expectativas
df_ge.expect_column_values_to_be_between('Glucose', min_value=0, max_value=200)
df_ge.expect_column_values_to_not_be_null('BloodPressure')
df_ge.expect_column_mean_to_be_between('Age', min_value=20, max_value=80)
for column in df.columns:
    df_ge.expect_column_values_to_not_be_null(column)
    df_ge.expect_column_values_to_be_in_type_list(
        column, ["int", "float", "string"])

# Adicione as expectativas à suite
suite.expectations = df_ge.get_expectation_suite(
    discard_failed_expectations=False)["expectations"]

# Salve o conjunto de expectativas
df_ge.save_expectation_suite("diabetes_expectations.json")

# Valide seu conjunto de dados em relação ao conjunto de expectativas
results = df_ge.validate(expectation_suite=suite)

# Converta o objeto de resultados em um dicionário
results_dict = results.to_json_dict()

# Salve os resultados em um arquivo JSON
with open('diabetes_results.json', 'w') as f:
    json.dump(results_dict, f)
