"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.links_personales import links_personales
from rxconfig import config
from link_bio.components.footer import footer
from link_bio.views.header.header import header


class State(rx.State):
    """The app state."""

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-center"),
        rx.vstack(
            navbar(),
            header(),
            rx.text(
                "Soy ingeniero en automatización (1 año de experiencia), me especializo en la creación de scripts para la automatización en procesos tanto en sistemas linux y windows.",
                size="7",
            ),
            links_personales(),
            spacing="5",
            justify="center",
            min_height="85vh",
            align_items="center"  # Corregido el typo (antes era "aling_items")
        ),
        footer(),
    )


app = rx.App()
app.add_page(index)