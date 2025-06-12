import reflex as rx
from datetime import datetime
from link_bio.components.links_personales import day_now
from link_bio.components.links_personales import mailto

def terms_of_service() -> rx.Component:
    return rx.vstack(
        rx.markdown(
            f"""# Términos de Servicio  

**Última actualización**: {day_now()}  

## 1. Aceptación de los Términos  
Al usar [blog Arnoldo del Toro](https://link-bio-gray-star.reflex.run/), aceptas estos términos. Si no estás de acuerdo, no uses el sitio.  

## 2. Uso Aceptable  
- Puedes navegar y compartir el contenido de manera personal.  
- No puedes:  
  - Copiar o plagiar el contenido sin permiso.  
  - Usar el sitio para fines ilegales o maliciosos.  

## 3. Propiedad Intelectual  
Todo el contenido (textos, imágenes, código) es propiedad de Arnoldo el Toro Peña, salvo que se indique lo contrario.  

## 4. Exclusión de Garantías  
El sitio se ofrece "como está". No garantizo que siempre funcione sin errores o interrupciones.  

## 5. Limitación de Responsabilidad  
No soy responsable por daños derivados del uso de este sitio.  

## 6. Enlaces Externos  
Los enlaces a terceros no implican respaldo. Su contenido y políticas son responsabilidad de sus propietarios.  

## 7. Modificaciones  
Puedo cambiar estos términos en cualquier momento. Los cambios serán efectivos al publicarlos aquí.  

## 8. Contacto  
Para dudas, escríbeme a: """
        ),
        mailto(),
        align="center",
        padding="1em",
        justify="center",
        width="100%"
    )