"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from link_bio.components.navbar import navbar
from rxconfig import config
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
from link_bio.views.base_page import base_page
from link_bio.pages.body import body
from link_bio.pages.privacy_legacy import privacy_legacy
from link_bio.pages.terms_of_service import terms_of_service
from link_bio.pages.to_do import todo_input

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

def terms() -> rx.Component:
    return base_page(
        terms_of_service()
    )

def todo() -> rx.Component:
    return base_page(
        todo_input()
    )

app = rx.App()
app.add_page(index)
app.add_page(privacy)
app.add_page(terms)
app.add_page(todo)