"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.links_personales import links_personales
from rxconfig import config
from link_bio.components.footer import footer
from link_bio.components.clock import card_clock 
from link_bio.views.header.header import header
import link_bio.styles.styles as styles




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
            "Soy ingeniero en automatización (1 año de experiencia), me especializo en la creación de scripts para la automatización en procesos tanto en sistemas linux y windows. Estoy en una activa búsqueda de trabajo. Cuento con 1 año de experiencia en procesos de trazabilidad de componentes.",
            size="7",
            ),
            card_clock(),
            links_personales(),
            footer(),
            
            spacing="4",
            justify="center",
            min_height="70vh",
            align_items="center",
        ),
    )


app = rx.App()
app.add_page(index)

