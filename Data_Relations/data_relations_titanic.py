from ydata_quality.data_relations import DataRelationsDetector
import pandas as pd
import numpy as np

# Carregar a base de dados Titanic
df = pd.read_csv(
    'C:/Users/ist.mevangelista/Documents/tcc/Datasets/Titanic/titanic.csv')

# Verificar e substituir valores nulos e infinitos
print("Valores nulos por coluna antes da limpeza:")
print(df.isnull().sum())
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)
print("Valores nulos por coluna após a limpeza:")
print(df.isnull().sum())

# Inicializar o detector de relações de dados
drd = DataRelationsDetector()

# Definir o dicionário de tipos de dados
dtype_dict = {
    'PassengerId': 'numerical',
    'Survived': 'numerical',
    'Pclass': 'numerical',
    'Name': 'categorical',
    'Sex': 'categorical',
    'Age': 'numerical',
    'SibSp': 'numerical',
    'Parch': 'numerical',
    'Ticket': 'categorical',
    'Fare': 'numerical',
    'Cabin': 'categorical',
    'Embarked': 'categorical'
}

# Função segura para cálculo de divisão


def safe_sqrt_division(phi_sq_hat, k_hat, r_hat):
    if k_hat <= 1 or r_hat <= 1:
        return np.nan
    return np.sqrt(phi_sq_hat / np.min([k_hat - 1, r_hat - 1]))


# Avaliar a base de dados com o módulo
try:
    results = drd.evaluate(df, dtype_dict)
except np.linalg.LinAlgError as e:
    print("Erro de convergência SVD:", e)
    results = None
except Exception as e:
    print("Erro durante a avaliação:", e)
    results = None

# Obter e imprimir os avisos
warnings = drd.get_warnings()
print("Avisos:")
print(warnings)

# Verificar se results foi definido
if results is not None:
    # Imprimir os resultados
    print("Resultados:")
    print(results)

    # Descomentar para imprimir resultados específicos
    # print("Confounders:")
    # print(results['Confounders'])

    # print("Colliders:")
    # print(results['Colliders'])

    # print("Feature Importance:")
    # print(results['Feature Importance'])

    # print("High Collinearity - Categorical:")
    # print(results['High Collinearity']['Categorical'])
else:
    print("A avaliação falhou e os resultados não foram gerados.")
