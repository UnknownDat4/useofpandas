import pandas as pd

path = '../data/'

def load_json(file_name):
    return pd.read_json(f'{path}{file_name}.json')

students = load_json('estudiantes')
neighborhoods = load_json('barrios')
subjects = load_json('materias')
notes = load_json('notas')


#¿Cuál es el promedio de edad de los estudiantes?
def average_students_ages():
    result = students["edad"].mean().round(1)
    return result

#¿Cuántos estudiantes viven en el barrio "San Benito"?
def san_benito_students():
    df_combined_data = students.merge(neighborhoods, on='identificacion', how='inner') # used for combining dataframes
    return len(df_combined_data[df_combined_data['barrio'] == 'San Benito']) # subquerie evaluation

# ¿Cuántos barrios están registrados?
def number_neighborhoods():
    result = len(neighborhoods['barrio'].value_counts())
    return result

# ¿Cuántos estudiantes aprobaron la materia "Base de Datos"?
def approved_database_subject():
    df_result = notes[(notes['nombre_materia'] == 'Base de Datos') & (notes['nota_final'] > 3)] # applying different conditions to a dataframe in order to filter data
    return df_result.shape[0]

# ¿Cuál es el promedio para la materia "Herramientas III"?
def tools3_Average():
    tools3_notes = notes[notes["nombre_materia"] == "Herramientas III"]
    final_note_average = tools3_notes["nota_final"].mean().round(1)
    return final_note_average

# ¿Cuál es la nota mínima de la materia "Ética y Valores"?
def minimum_grade():
    df_result = notes[(notes['nombre_materia'] == 'Ética y Valores')]
    return df_result['nota_final'].min()

# ¿Cuántos estudiantes que vivan en el barrio "Guayaquil" han obtenido un promedio general por encima de 3.8?

def high_performing_guayaquil_students():
    average_students_note = notes[["identificacion","nota_final"]].groupby("identificacion").mean().round(1)
    guayaquil_students = neighborhoods[neighborhoods["barrio"] == "Guayaquil"]
    note_guayaquil_students = average_students_note.merge(guayaquil_students, how="inner", on="identificacion")
    result = len(note_guayaquil_students[note_guayaquil_students["nota_final"] > 3.8])
    return result


# ¿Cuál es la materia con mayor cantidad de estudiantes que han reprobado?
def subjects_failed():
    df_result = notes.query("nota_final < 3").groupby('nombre_materia')['nota_final'].count()
    materia = df_result.idxmax()
    reprobados = int(df_result.max())
    return materia, reprobados

# ¿Cuál o cuáles materias no han sido matriculadas por los estudiantes?


print(f"- el promedio de edad de los estudiantes es de {average_students_ages()}")
print(f"- {san_benito_students()} estudiantes viven en el barrio San Benito")
print(f"- hay {number_neighborhoods()} barrios registrados")
print(f"- {approved_database_subject()} estudiantes aprobaron la materia Base de Datos")
print(f"- el promedio para la materia Herramientas III es {tools3_Average()}")
print(f"- la nota mínima de la materia Ética y Valore es de {minimum_grade()}")
print(f"- {high_performing_guayaquil_students()} estudiantes que vivan en Guayaquil han obtenido un promedio general por encima de 3.8")

subjects_failed_result = subjects_failed()
print(f"- la materia con mayor cantidad de estudiantes que han reprobado es {subjects_failed_result[0]} con {subjects_failed_result[1]} repropados")
