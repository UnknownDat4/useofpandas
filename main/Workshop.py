import pandas as pd

path = '../data/'

def load_json(file_name):
    return pd.read_json(f'{path}{file_name}.json')

students = load_json('estudiantes')
neighborhoods = load_json('barrios')
subjects = load_json('materias')
notes = load_json('notas')


#¿Cuál es el promedio de edad de los estudiantes?

#¿Cuántos estudiantes viven en el barrio "San Benito"?
def san_benito_students():
    df_combined_data = students.merge(neighborhoods, on='identificacion', how='inner') # used for combining dataframes
    return len(df_combined_data[df_combined_data['barrio'] == 'San Benito']) # subquerie evaluation

# ¿Cuántos barrios están registrados?

# ¿Cuántos estudiantes aprobaron la materia "Base de Datos"?
def approved_database_subject():
    df_result = notes[(notes['nombre_materia'] == 'Base de Datos') & (notes['nota_final'] > 3)] # applying different conditions to a dataframe in order to filter data
    return df_result.shape[0]

# ¿Cuál es el promedio para la materia "Herramientas III"?

# ¿Cuál es la nota mínima de la materia "Ética y Valores"?
def minimum_grade():
    df_result = notes[(notes['nombre_materia'] == 'Ética y Valores')]
    return df_result['nota_final'].min()

# ¿Cuántos estudiantes que vivan en el barrio "Guayaquil" han obtenido un promedio general por encima de 3.8?

# ¿Cuál es la materia con mayor cantidad de estudiantes que han reprobado?
def subjects_failed():
    df_result = notes.query("nota_final < 3").groupby('nombre_materia')['nota_final'].count()
    materia = df_result.idxmax()
    reprobados = int(df_result.max())
    return materia, reprobados

# ¿Cuál o cuáles materias no han sido matriculadas por los estudiantes?




print(f"- {san_benito_students()} estudiantes viven en el barrio San Benito")

print(f"- {approved_database_subject()} estudiantes aprobaron la materia Base de Datos")

print(f"- la nota mínima de la materia Ética y Valore es de {minimum_grade()}")

subjects_failed_result = subjects_failed()
print(f"- la materia con mayor cantidad de estudiantes que han reprobado es {subjects_failed_result[0]} con {subjects_failed_result[1]} repropados")
