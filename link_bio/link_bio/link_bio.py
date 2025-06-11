"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from link_bio.components.navbar import navbar
from rxconfig import config
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
from link_bio.views.base_page import base_page
from link_bio.pages.body import body
from link_bio.pages.privacy_legacy import privacy_legacy

class State(rx.State):
    """The app state."""

def index() -> rx.Component:
    # Welcome Page (Index)
    return base_page(
            body()
        )

def privacy() -> rx.Component:
    return base_page(
            privacy_legacy()
        )  

app = rx.App()
app.add_page(index)
app.add_page(privacy)

