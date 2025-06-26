import reflex as rx

def header():
    return rx.hstack(  # Usamos hstack para alinear horizontalmente
        rx.image(
            src="/file.jpg",
            width="200px",
            height="auto",
            border_radius="15px 50px",
            border="5px solid #555",
            margin_right="2rem"  # Espacio horizontal a la derecha
        ),
        rx.heading("🙃 Bienvenid@. Mi nombre es Arnoldo Del Toro!", size="9"),
        align="center",  # Centramos verticalmente los elementos
    ),

