import pandas as pd
from pathlib import Path

#FIXME: AGREGAR ESTAS VARIABLES Y FUNCIONES EN UNA CLASE
"""local variables"""
db_local_path = "link_bio/views/App_To_Do/bd_local.csv"
estados = ["eliminada", "pendiente", "completada"]

"""funciones"""
def open_csv(archivo_csv:str=db_local_path, first_time:bool=True):
    """función para abrir el archivo csv local

    Args:
        archivo_csv (csv): archivo csv db_local.csv
        first_time (bool, optional): se usa para definir cuando se manda llamar por primera vez. Defaults to True.

    Returns:
        pd.DataFrame: regresa un data frame con las tareas almacenadas. 
    """    
    if not archivo_csv_existe(archivo_csv):
        print("Creando archivo db_local.csv")
        create_csv()
    df = pd.read_csv(archivo_csv, encoding="utf-8")
    print("Tareas leídas correctamente")
    if first_time:
        print(df)
    return df

def archivo_csv_existe(archivo_csv):
    """verifica la existencia del archivo"""
    return Path(archivo_csv).exists()

def create_csv(nombre="link_bio/views/App_To_Do/bd_local.csv"):
    """funcion para crear el archivo si es que no existe"""
    data_default = {"id": [1], "tarea": ["Mirar mi Web"], "estado": ["completada"]}
    df = pd.DataFrame(data_default)
    df.to_csv(nombre, index=False, encoding="utf-8")
    return print("db_local.csv creado ...")

def new_task(task: str):
    df = open_csv(first_time=False)
    _id = df["id"].iloc[-1] + 1
    _estado = "pendiente"
    nuevo_registro = [_id, task, _estado]
    nuevo_registro_df = pd.DataFrame(
        [nuevo_registro], columns=["id", "tarea", "estado"]
    )
    df = pd.concat([df, nuevo_registro_df], ignore_index=True)
    save_csv(df)
    return print(f"Nueva tarea agregada: {nuevo_registro[1]}")

def view_pending_tasks(archivo_csv):
    """Leer las tareas pendientes desde el archivo csv"""
    pass

def view_completed_tasks(archivo_csv):
    """Leer las tareas eliminadas desde el archivo csv"""
    pass

def save_csv(new_data_frame, archivo_csv=db_local_path):
    new_data_frame.to_csv(archivo_csv, index=False, encoding='utf-8')

def complete_task(task):
    df = open_csv(first_time=False)
    df.loc[df['tarea'] == task, 'estado'] = 'completada'
    save_csv(df)
    
if __name__ == "__main__":
    open_csv()
    
    #TODO: cuando se cree el botón check in en la app no habrá un input, la idea es que tome el str del mismo botón.
    #task_new = input("Ingresa la nueva tarea: ")
    #new_task(task_new)
    tarea_completada = str(input(f"introduzca la tarea a eliminar: "))
    complete_task(tarea_completada)

