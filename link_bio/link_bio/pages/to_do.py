import reflex as rx
from link_bio.views.base_page import base_page

class FormInputState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def todo_input():
    return rx.vstack(
        rx.heading("Anota aquí todas tus tareas: 😁"), 
        rx.form.root(
            rx.vstack(
            rx.input(name="task", placeholder="Introduce la nueva tarea", type="text", required=True, size="3", ),
            rx.button("Agregar",type="submit",),
            align_items="center",
            ),
            on_submit=FormInputState.handle_submit,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Tareas por terminar: 😇"),
        rx.badge(FormInputState.form_data),
        align_items="center",
        width="100%"
    )



# rx.card(
#         rx.vstack(
#             rx.heading("Example Form"),
#             rx.form.root(
#                 rx.hstack(
#                     rx.input(
#                         name="input",
#                         placeholder="Enter text...",
#                         type="text",
#                         required=True,
#                     ),
#                     rx.button("Submit", type="submit"),
#                 ),
#                 on_submit=FormInputState.handle_submit,
#                 reset_on_submit=True,
#                 align_items="center",
#             ),
#             rx.divider(),
#             rx.hstack(
#                 rx.heading("Results:"),
#                 rx.badge(
#                     FormInputState.form_data.to_string() # type: ignore
#                 ), 
#             ), 
#             align_items="center",
#         ),
#         align_content="center",  
#         width="100%",
#     )