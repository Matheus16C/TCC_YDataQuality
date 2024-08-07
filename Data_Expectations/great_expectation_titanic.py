import pandas as pd
import json
import great_expectations as ge
from great_expectations.core.expectation_suite import ExpectationSuite

df = pd.read_csv(
    'C:/Users/ist.mevangelista/Documents/tcc/Datasets/Titanic/titanic.csv')

# Converta o DataFrame do pandas em um DataFrame do Great Expectations
df_ge = ge.from_pandas(df)

# Crie um novo conjunto de expectativas
suite = ExpectationSuite(expectation_suite_name="titanic_expectations")

df_ge.expect_column_mean_to_be_between('Age', min_value=0, max_value=80)
df_ge.expect_column_mean_to_be_between('Survived', min_value=0, max_value=1)
df_ge.expect_column_mean_to_be_between('Pclass', min_value=1, max_value=3)
for column in df.columns:
    df_ge.expect_column_values_to_not_be_null(column)
    df_ge.expect_column_values_to_be_in_type_list(
        column, ["int", "float", "string"])

# Adicione as expectativas à suite
suite.expectations = df_ge.get_expectation_suite(
    discard_failed_expectations=False)["expectations"]

# Salve o conjunto de expectativas
df_ge.save_expectation_suite("titanic_expectations.json")

# Valide seu conjunto de dados em relação ao conjunto de expectativas
results = df_ge.validate(expectation_suite=suite)

# Converta o objeto de resultados em um dicionário
results_dict = results.to_json_dict()

# Salve os resultados em um arquivo JSON
with open('titanic_results.json', 'w') as f:
    json.dump(results_dict, f)
