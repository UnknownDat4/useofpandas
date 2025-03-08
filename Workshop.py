import pandas as pd

path = 'C:/Users/jhntn/OneDrive/Documentos/Python/Pandas/'

def load_json(file_name):
    return pd.read_json(f'{path}{file_name}.json')

estudiantes = load_json('estudiantes')
barrios = load_json('barrios')
materias = load_json('materias')
notas = load_json('notas')

def get_average_age():
    return estudiantes['edad'].median() # obtains the average value

def san_benito_students():
    df_combined_data = estudiantes.merge(barrios, on='identificacion', how='inner') # used for combining dataframes
    return len(df_combined_data[df_combined_data['barrio'] == 'San Benito']) # subquerie evaluation

def count_registered_neighborhoods():
    return barrios['barrio'].nunique() # used for counting disntict elements

def approved_database_subject():
    df_result = notas[(notas['nombre_materia'] == 'Base de Datos') & (notas['nota_final'] > 3)] # applying different conditions to a dataframe in order to filter data
    return df_result.shape[0]

def hp3_average_grades():
    df_result = notas[(notas['nombre_materia'] == 'Herramientas III')]
    return df_result['nota_final'].median()

def minimum_grade():
    df_result = notas[(notas['nombre_materia'] == 'Ética y Valores')]
    return df_result['nota_final'].min()

def above_average():
    df_combined_data = estudiantes.merge(barrios, on='identificacion', how='inner').query("barrio == 'Guayaquil'") 
    df_aboveavg = pd.DataFrame(df_combined_data.merge(notas, on='identificacion', how='inner').groupby('identificacion', as_index = False)['nota_final'].median())
    return df_aboveavg.query("nota_final > 3.8").shape[0]

def subjects_failed():
    df_result = notas.query("nota_final < 3").groupby('nombre_materia')['nota_final'].count()
    materia = df_result.idxmax()  # Obtiene el nombre de la materia con más reprobados
    reprobados = int(df_result.max())
    return materia, reprobados

print(subjects_failed())
