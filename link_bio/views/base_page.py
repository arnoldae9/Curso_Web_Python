import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer

def base_page(child: rx.Component, *args, **kargs) -> rx.Component:
    return rx.fragment(
        rx.color_mode.button(position="top-center"),
        rx.vstack(
            navbar(),
            child,
            footer(),
        ),
    )