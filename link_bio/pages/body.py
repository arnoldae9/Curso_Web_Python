import reflex as rx
from link_bio.components.links_personales import links_personales
from link_bio.components.clock import card_clock 
from link_bio.views.header.header import header
from link_bio.views.quotes import quote
from link_bio.pages.main_text import texto_principal

def body() -> rx.Component:
    return rx.vstack(
        header(),
        texto_principal(),
        links_personales(),
        card_clock(),
        quote(),
        spacing="4",
        justify="center",
        min_height="70vh",
        align_items="center",
    )