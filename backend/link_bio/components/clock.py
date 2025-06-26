import reflex as rx
from datetime import datetime

class TemporalState(rx.State):
    current_time: str = ""

    @rx.event
    def update_time(self):
        self.current_time = (
            datetime.now().strftime("%H:%M:%S")
        )


def clock():
    return rx.vstack(
        rx.heading(TemporalState.current_time),
        rx.moment(
            interval=1000,
            on_change=TemporalState.update_time.temporal,
        ),
        align="center"
    )

def card_clock() -> rx.Component:
    return rx.card(clock(), size="1") # size 1 2 3 4 5
