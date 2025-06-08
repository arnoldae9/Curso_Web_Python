"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-center"),
        rx.vstack(
            rx.hstack(  # Usamos hstack para alinear horizontalmente
                rx.image(
                    src="/file.jpg",
                    width="200px",
                    height="auto",
                    border_radius="15px 50px",
                    border="5px solid #555",
                    margin_right="2rem"  # Espacio horizontal a la derecha
                ),
                rx.heading("👋🏼 Hola. Mi nombre es Arnoldo Del Toro!", size="9"),
                align="center",  # Centramos verticalmente los elementos
            ),
            rx.text(
                "Soy ingeniero en automatización (1 año de experiencia), me especializo en la creación de scripts para la automatización en procesos tanto en sistemas linux y windows.",
                size="7",
            ),
            rx.hstack(
            rx.link(
                rx.hstack(
                rx.icon(tag="github"),
                rx.button("Link a mi Github !! 😊"),
                spacing="2"
                ),
                href="https://github.com/arnoldae9",
                is_external=True,
            ),
            rx.link(
                rx.hstack(
                    rx.icon(tag="file-text"),
                    rx.button("Descarga mi cv !! 😁", color_scheme="red"),
                    spacing="2"
                ),
                href="/cv.pdf",
                is_external=False,
                download="Cv_Arnoldo_Del_Toro_Peña.pdf"
            ),
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            align_items="center"  # Corregido el typo (antes era "aling_items")
        ),
    )


app = rx.App()
app.add_page(index)