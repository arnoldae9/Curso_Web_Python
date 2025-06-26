import reflex as rx

def texto_principal ():
    return rx.vstack(
        rx.text("Soy ingeniero en automatización (1 año de experiencia), me especializo en la creación de scripts para la automatización en procesos tanto en sistemas linux y windows. Estoy en una activa búsqueda de trabajo. Cuento con 1 año de experiencia en procesos de trazabilidad de componentes.",
        size="7",
        width="90%",
        ),
        rx.hstack(
        rx.text("Me puedes contactar al siguiente correo: arnoldae9@gmail.com", size="7"),
        rx.button(
        "Copiar Email",
        on_click=rx.set_clipboard("arnoldae9@gmail.com"),
        color_scheme="blue",
        _hover={"color": "blue"},
        ),
        align_items="center",
        ),
        justify="center",
        align_items="center",
    )