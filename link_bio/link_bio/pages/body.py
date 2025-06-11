import reflex as rx
from link_bio.components.links_personales import links_personales
from link_bio.components.clock import card_clock 
from link_bio.views.header.header import header
from link_bio.views.quotes import quote


def body() -> rx.Component:
    return rx.vstack(
            quote(),
            header(),
            card_clock(),
            rx.text("Soy ingeniero en automatización (1 año de experiencia), me especializo en la creación de scripts para la automatización en procesos tanto en sistemas linux y windows. Estoy en una activa búsqueda de trabajo. Cuento con 1 año de experiencia en procesos de trazabilidad de componentes.",
                size="7",
                width="90%"
            ),
            links_personales(),
            spacing="4",
            justify="center",
            min_height="70vh",
            align_items="center",

    )