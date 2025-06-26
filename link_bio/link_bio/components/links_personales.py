import reflex as rx
from datetime import datetime

def day_now():
    return datetime.now().strftime('%d de %B de %Y, %H:%M:%S')

def mailto() -> rx.Component:
    return rx.link("arnoldae9@gmail.com", href="mailto:arnoldae9@gmail.com?subject=Consulta desde la pagina Web Arnoldo Del Toro.")

def links_personales() :
    return rx.hstack(
        rx.link(
            rx.hstack(
            rx.icon(tag="github", color="gray"),
            rx.button("Link a mi Github !! 😊", color_scheme="gray", _hover={"color": "blue"}),
            spacing="2"
            ),
            href="https://github.com/arnoldae9",
            is_external=True,
        ),
        rx.link(
            rx.hstack(
                rx.icon(tag="file-text", color="red"),
                rx.button("Descarga mi cv !! 😁", color_scheme="red", _hover={"color": "blue"}),
                spacing="2"
            ),
            href="/cv.pdf",
            is_external=False,
            download="Cv_Arnoldo_Del_Toro_Peña.pdf"
        ),
        rx.link(
            rx.hstack(
            rx.icon(tag="file-text", color="red"),
            rx.button("Ver mi CV 👁️", color_scheme="red", _hover={"color": "blue"}),
            ),
            href="/cv.pdf",
            is_external=True  # Abre en nueva pestaña
        ),
        rx.link(
            rx.hstack(
                rx.icon(tag="linkedin", color="blue"),
                rx.button("Link a Linkedin!! 😄", color_scheme="blue", _hover={"color": "blue"}),
                spacing="2"
            ),
            href="http://www.linkedin.com/in/arnoldo-del-toro-ba0468255",
            is_external=True,
        ),
        # rx.link(
        #     rx.hstack(
        #         rx.icon(tag="twitter", color="sky"),
        #         rx.button("Link a twitter !! 😁", color_scheme="sky", _hover={"color": "blue"}),
        #         spacing="2"
        #     ),
        #     href="http://www.x.com/ARNOLDdeltoro1",
        #     is_external=True,
        # ),
        ),
