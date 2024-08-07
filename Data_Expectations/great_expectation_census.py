import pandas as pd
import json
import great_expectations as ge
from great_expectations.core.expectation_suite import ExpectationSuite

df = pd.read_csv(
    'C:/Users/ist.mevangelista/Documents/tcc/Datasets/Census/Census_50k.csv')

# Converta o DataFrame do pandas em um DataFrame do Great Expectations
df_ge = ge.from_pandas(df)

# Crie um novo conjunto de expectativas
suite = ExpectationSuite(expectation_suite_name="census_expectations")

# Adicione suas expectativas
df_ge.expect_column_values_to_be_between('age', 17, 90)
df_ge.expect_column_values_to_be_in_set('workclass', [
    'Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay', 'Never-worked'])
# Limites ajustados para remover valores extremos
df_ge.expect_column_values_to_be_between('fnlwgt', 1000, 1500000)
df_ge.expect_column_values_to_be_in_set('education', ['Bachelors', 'Some-college', '11th', 'HS-grad', 'Prof-school',
                                                      'Assoc-acdm', 'Assoc-voc', '9th', '7th-8th', '12th', 'Masters', '1st-4th', '10th', 'Doctorate', '5th-6th', 'Preschool'])
df_ge.expect_column_values_to_be_between('education-num', 1, 16)
df_ge.expect_column_values_to_be_in_set('marital-status', ['Married-civ-spouse', 'Divorced',
                                                           'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent', 'Married-AF-spouse'])
df_ge.expect_column_values_to_be_in_set('occupation', ['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty',
                                                       'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces'])
df_ge.expect_column_values_to_be_in_set('relationship', [
    'Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried'])
df_ge.expect_column_values_to_be_in_set(
    'race', ['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black'])
df_ge.expect_column_values_to_be_in_set('sex', ['Female', 'Male'])
df_ge.expect_column_values_to_be_between(
    'capital-gain', 0, 99999)  # Evitando valores negativos
df_ge.expect_column_values_to_be_between(
    'capital-loss', 0, 4356)  # Evitando valores negativos
df_ge.expect_column_values_to_be_between(
    'hours-per-week', 1, 99)  # Valores entre 1 e 99
df_ge.expect_column_values_to_be_in_set('native-country', ['United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada', 'Germany', 'Outlying-US(Guam-USVI-etc)', 'India', 'Japan', 'Greece', 'South', 'China', 'Cuba', 'Iran', 'Honduras', 'Philippines', 'Italy', 'Poland', 'Jamaica',
                                                           'Vietnam', 'Mexico', 'Portugal', 'Ireland', 'France', 'Dominican-Republic', 'Laos', 'Ecuador', 'Taiwan', 'Haiti', 'Columbia', 'Hungary', 'Guatemala', 'Nicaragua', 'Scotland', 'Thailand', 'Yugoslavia', 'El-Salvador', 'Trinadad&Tobago', 'Peru', 'Hong', 'Holand-Netherlands'])
df_ge.expect_column_values_to_be_in_set('income', ['<=50K', '>50K'])
for column in df.columns:
    df_ge.expect_column_values_to_not_be_null(column)
    df_ge.expect_column_values_to_be_in_type_list(
        column, ["int", "float", "string"])

# Adicione as expectativas à suite
suite.expectations = df_ge.get_expectation_suite(
    discard_failed_expectations=False)["expectations"]

# Salve o conjunto de expectativas
df_ge.save_expectation_suite("census_expectations.json")

# Valide seu conjunto de dados em relação ao conjunto de expectativas
results = df_ge.validate(expectation_suite=suite)

# Converta o objeto de resultados em um dicionário
results_dict = results.to_json_dict()

# Salve os resultados em um arquivo JSON
with open('census_results.json', 'w') as f:
    json.dump(results_dict, f)
