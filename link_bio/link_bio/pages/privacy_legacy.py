import reflex as rx
from datetime import datetime
from link_bio.components.links_personales import mailto
from link_bio.components.links_personales import day_now

def privacy_legacy() -> rx.Component:
    return rx.vstack(
        rx.markdown(
            f"""# Política de Privacidad  

**Última actualización**: {day_now()}

Esta es la política de privacidad de Arnoldo Del Toro Peña.  

## 1. Datos que Recopilo  
- Si me contactas vía formulario, guardo tu nombre y correo para responder.  
- Uso Google Analytics para ver estadísticas anónimas de visitas (IP, navegador, páginas visitadas).  

## 2. Cookies  
Este sitio usa cookies de analytics. Puedes desactivarlas en tu navegador.  

## 3. Terceros  
No comparto tus datos con terceros, pero uso servicios como:  
- GitHub Pages (hosting). 
- Reflex (hosting).
- Cloudflare (hosting) 
- Google Analytics (estadísticas).  

## 4. Tus Derechos  
Puedes pedirme eliminar tus datos de contacto enviándome un correo.  

## 5. Cambios  
Esta política puede actualizarse. Revisa esta página para cambios.  

"""           
        ),
        rx.text("Contacto: ", as_="span"),
        mailto(),
        align="center",
        padding="1em",
        justify="center",
        width="100%"
    )
