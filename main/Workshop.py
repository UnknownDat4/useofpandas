import pandas as pd

path = '../data/'

def load_json(file_name):
    return pd.read_json(f'{path}{file_name}.json')

estudiantes = load_json('estudiantes')
barrios = load_json('barrios')
materias = load_json('materias')
notas = load_json('notas')


def san_benito_students():
    df_combined_data = estudiantes.merge(barrios, on='identificacion', how='inner') # used for combining dataframes
    return len(df_combined_data[df_combined_data['barrio'] == 'San Benito']) # subquerie evaluation

def approved_database_subject():
    df_result = notas[(notas['nombre_materia'] == 'Base de Datos') & (notas['nota_final'] > 3)] # applying different conditions to a dataframe in order to filter data
    return df_result.shape[0]

def minimum_grade():
    df_result = notas[(notas['nombre_materia'] == 'Ética y Valores')]
    return df_result['nota_final'].min()

def subjects_failed():
    df_result = notas.query("nota_final < 3").groupby('nombre_materia')['nota_final'].count()
    materia = df_result.idxmax()
    reprobados = int(df_result.max())
    return materia, reprobados
