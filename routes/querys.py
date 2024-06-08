from fastapi import APIRouter , Request, Form, HTTPException


from fastapi.responses import HTMLResponse, RedirectResponse
import mysql.connector
from mysql.connector import Error

from config.db import create_connection

user = APIRouter()

header_html = """

"""

footer_html = """   
  <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js' integrity='sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz' crossorigin='anonymous'></script>
  </body>
</html>
"""

@user.post("/ConsultaPeli")
async def ConsulaPeliculas(request: Request, Titulo: str = Form(...)):

  
  headerMOvies= """"
        <!doctype html>
    <html lang='en'>
      <head>
      <meta charset='utf-8'>
      <meta name='viewport' content='width=device-width, initial-scale=1'>
      <title>Medallero</title>
      <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH' crossorigin='anonymous'>
      <link rel="stylesheet" href="static/css/styles.css">

      </head>
      <body>
        """

  print(Titulo)
    
  conn = create_connection("localhost", "root", "root", "movies")

  cursor = conn.cursor()

  cursor.execute(f"""SELECT M.title, M.overview, TRUNCATE(M.popularity,2), M.release_date,M.vote_average FROM movie as M 
        WHERE M.title like '%{Titulo}%'  LIMIT 5;""")
  

  result = "<table class='table table-hover'>"
  result += "<tr><th>IMAGEN</th><th>TITULO</th><th>SINOPSIS</th><th>POPULARIDAD</th><th>LANZAMIENTO</th><th>APROVACION</th></tr>"

  rows= cursor.fetchall() 

  for row in rows:
             
             result += "<td><img src='static/images/imagen5.jpg' alt='Imagen 3' style='width: 100px; height: 100px;'></td>"
             result += "<td>" + str(row[0])  + "</td>"
             result += "<td> " + str(row[1])+ "</td>"
             result += "<td> " + str(row[2])+ "</td> "
             result += "<td> " + str(row[3])+ "</td> "
             result += "<td> " + str(row[4])+ "</td><tr> "

  
  result += "</table>"  

  result += '<a href="/menuU" class="mi-boton">Haz Clic Aquí</a>'

  conn.commit()
  conn.close()

  return HTMLResponse(content=headerMOvies + result + footer_html, status_code=200)
  
