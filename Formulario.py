
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_correo(destinatario, asunto, mensaje_html):
    # Configurar los detalles del remitente
    remitente = 'tu_correo@gmail.com'
    contraseña = 'tu_contraseña'

    # Crear objeto MIME
    mensaje = MIMEMultipart('alternative')
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto

    # Crear partes del mensaje
    mensaje_texto = MIMEText(mensaje_html, 'html')

    # Adjuntar partes del mensaje al objeto MIME
    mensaje.attach(mensaje_texto)

    # Conectar al servidor SMTP de Gmail
    servidor_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    servidor_smtp.starttls()
    servidor_smtp.login(remitente, contraseña)

    # Enviar el correo electrónico
    servidor_smtp.sendmail(remitente, destinatario, mensaje.as_string())

    # Cerrar la conexión SMTP
    servidor_smtp.quit()

# Ejemplo de uso
destinatario = 'anthonyospinafernandez@gmail.com'
asunto = '¡Deseo unirme a la comunidad!'
mensaje_html = '''
<html>
<head></head>
<body>
    <h1>Bienvenido a la comunidad</h1>
    <p>Ingresa el mensaje para ser respondido posteriormente</p>
    <p>Gracias por tus datos</p>
</body>
</html>
'''

enviar_correo(destinatario, asunto, mensaje_html)
