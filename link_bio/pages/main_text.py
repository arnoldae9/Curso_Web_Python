import reflex as rx

def texto_principal ():
    return rx.vstack(
        rx.text("Soy ingeniero en automatización (1 año de experiencia), me especializo en la creación de scripts para la automatización en procesos tanto en sistemas linux y windows. Estoy en una activa búsqueda de trabajo. Cuento con 1 año de experiencia en procesos de trazabilidad de componentes. \n Mi principal proyecto es el despliegue, mantenimiento y soporte de un sistema de trazabilidad de componentes y la automatización de los scripts para el sistema.",
        size="7",
        width="90%",
        ),
        rx.text("Puede consultar mis proyectos en desarrollo en mis repositorios públicos en GitHub.", size="7", width="90%"),
        rx.text("Me puedes contactar al siguiente correo:", size="7", width="90%"),
        rx.hstack(
        rx.text("arnoldae9@gmail.com", size="7"),
        rx.button(
        "Copiar Email",
        on_click=rx.set_clipboard("arnoldae9@gmail.com"),
        color_scheme="blue",
        _hover={"color": "blue"},
        ),
        align_items="center",
        ),
        justify="start",
        align_items="center",
    )