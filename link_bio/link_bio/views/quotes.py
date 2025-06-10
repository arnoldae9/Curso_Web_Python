import reflex as rx
import httpx

class QuoteState(rx.State):
    """Estado para manejar las citas aleatorias."""
    quote: str = "Presiona el botón para obtener una cita inspiradora"
    author: str = ""
    loading: bool = False

    async def get_random_quote(self):
        self.loading = True
        yield
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get("http://api.quotable.io/quotes/random",
                params={"language": "es"} 
                )
                if response.status_code == 200:
                    data = response.json()[0]
                    self.quote = data["content"]
                    self.author = data["author"]
                else:
                    self.quote = "Error al obtener la cita"
                    self.author = ""
        except Exception as e:
            self.quote = f"Error de conexión: {str(e)}"
            self.author = ""
        
        self.loading = False

def quote_component() -> rx.Component:
    """Componente que muestra una cita aleatoria."""
    return rx.card(
        rx.vstack(
            rx.cond(
                QuoteState.loading,
                rx.spinner(size="1"),
                rx.vstack(
                    rx.text(QuoteState.quote, size="5", font_style="italic"),
                    rx.text(f"— {QuoteState.author}", size="3", color="gray"),
                    spacing="2",
                    align_items="start",
                ),
            ),
            rx.button(
                "Obtener nueva cita",
                on_click=QuoteState.get_random_quote,
                is_loading=QuoteState.loading,
                width="100%",
                margin_top="1em",
            ),
            spacing="3",
        ),
        width="100%",
        max_width="600px",
        padding="1em",
    )

def quote() -> rx.Component:
    return  rx.center(
                quote_component(),
                width="100%",
                padding="2em 0",
            ),