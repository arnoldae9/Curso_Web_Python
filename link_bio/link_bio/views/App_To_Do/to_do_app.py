import pandas as pd
from pathlib import Path

# FIXME: Crear una función que cree el archivo csv si no existe...

#FIXME: AGREGAR ESTAS VARIABLES Y FUNCIONES EN UNA CLASE
class TODO():
    def __init__(self, new_db_local: pd.DataFrame = pd.DataFrame(), task: str = "",):
        """local variables"""
        db_local_path = "link_bio/views/App_To_Do/bd_local.csv"
        # estados = ["eliminada", "pendiente", "completada"]
        self.ruta_csv = db_local_path
        self.task = task
        self.new_db_local = new_db_local
        self.archivo_csv = pd.read_csv(self.ruta_csv, encoding="utf-8")

    # FIXME: estas funcion tiene que ser fuera de la clase...        
    def archivo_csv_existe(self):
        """verifica la existencia del archivo retorna un booleano"""
        return Path(self.ruta_csv).exists()

    def create_csv(self):
        """función para crear el archivo si es que no existe"""
        data_default = {"id": [1], "tarea": ["Mirar mi Web"], "estado": ["pendiente"]}
        df = pd.DataFrame(data_default)
        df.to_csv(self.ruta_csv, index=False, encoding="utf-8")
        return print("db_local.csv creado ...")
    # FIXME: Hasta aquí ...

    def new_task(self):
        #df = open_csv(first_time=False)
        _id = self.archivo_csv["id"].iloc[-1] + 1
        _estado = "pendiente"
        nuevo_registro = [_id, self.task, _estado]
        nuevo_registro_df = pd.DataFrame(
            [nuevo_registro], columns=["id", "tarea", "estado"]
        )
        self.new_db_local = pd.concat([self.archivo_csv, nuevo_registro_df], ignore_index=True)
        self.new_db_local.to_csv(self.ruta_csv, index=False, encoding='utf-8')
        return print(f"Nueva tarea agregada: {nuevo_registro[1]}")

    def view_pending_tasks(self):
        """Leer las tareas pendientes desde el archivo csv, la idea es que regrese un data frame filtrado"""
        # archivo_csv=open_csv(first_time=False)
        return print(self.archivo_csv[self.archivo_csv["estado"]=="pendiente"].to_string(index=False))
        

    def view_completed_tasks(self):
        """Leer las tareas completadas desde el archivo csv, el objetivo es mostrar las completadas"""
        return print(self.archivo_csv[self.archivo_csv["estado"]=="completada"].to_string(index=False))

    def task_to_complete(self):
        self.archivo_csv.loc[self.archivo_csv['tarea'] == self.task, 'estado'] = 'completada'
        self.archivo_csv.to_csv(self.ruta_csv, encoding="utf-8")

    def task_to_pending(self):
        self.archivo_csv.loc[self.archivo_csv['tarea'] == self.task, 'estado'] = 'pendiente'
        self.archivo_csv.to_csv(self.ruta_csv, encoding="utf-8")
        
if __name__ == "__main__":
    # pasos para nueva tarea 
    # tarea_nueva = input("Ingresa la tarea nueva: ")
    # todo = TODO(task=tarea_nueva)
    # todo.new_task()
    #---------------------------#
    # pasos para los views
    # todo = TODO()
    # todo.view_completed_tasks()
    # todo.view_pending_tasks()
    #---------------------------#
    # pasos para completar tareas
    # tarea_a_eliminar = input("Ingrese la tarea a completar: ")
    # todo = TODO(task=tarea_a_eliminar)
    # todo.complete_task()
    #---------------------------#
    # pasos para tareas pendientes
    tarea_pendiente = input("Ingrese la tarea pendiente: ")
    todo = TODO(task=tarea_pendiente)
    todo.task_to_pending()
    #---


    # open_csv()
    # TODO: cuando se cree el botón check in en la app no habrá un input, la idea es que tome el str del mismo botón.
    # task_new = input("Ingresa la nueva tarea: ")
    # new_task(task_new)
    # tarea_completada = str(input(f"introduzca la tarea a eliminar: "))
    # complete_task(tarea_completada)
    # view_pending_tasks()
    # view_completed_tasks()

