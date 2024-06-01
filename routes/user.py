from fastapi import APIRouter , Request, Form, HTTPException


from fastapi.responses import HTMLResponse
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

@user.get("/")
async def read_root():
	html_content = header_html + """
     
     <!doctype html>
<html lang='en'>
  <head>
	<meta charset='utf-8'>
	<meta name='viewport' content='width=device-width, initial-scale=1'>
	<title>Medallero</title>
	<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH' crossorigin='anonymous'>
  <link rel="stylesheet" href="static/css/MainMenu.css">

  </head>
  <body>
    <nav class='navbar navbar-expand-lg bg-body-tertiary'>
    <div class='container-fluid'>
	<a class='navbar-brand' href='http://www.google.com'>Gravity</a>
	<button class='navbar-toggler' type='button' data-bs-toggle='collapse' data-bs-target='#navbarSupportedContent' aria-controls='navbarSupportedContent' aria-expanded='false' aria-label='Toggle navigation'>
  	<span class='navbar-toggler-icon'></span>
	</button>
	<div class='collapse navbar-collapse' id='navbarSupportedContent'>
  	<!-- unordered list  ul	list item li-->
  	<ul class='navbar-nav me-auto mb-2 mb-lg-0'>
    	<li class='nav-item'>
      	<a class='nav-link active' aria-current='page' href='/InsertarPagina'>Medallero</a>
    	</li>
    	<li class='nav-item'>
      	<a class='nav-link' href='/movies'>Deportistas</a>
    	</li>
    	<li class='nav-item'>
      	<a class='nav-link' href='/InsertarPagina'>Sedes</a>
    	</li>   	 
  	</ul>
       
	</div>
     </div>

     <div class="logoUno">
            <img src="/static/images/logo.png" alt="bot">
        </div>
    </nav>""" + footer_html
    
	return HTMLResponse(content=html_content, status_code=200)


@user.get("/movies")
async def helloWorld():
    
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

    try:
        conn = create_connection("localhost", "root", "root", "PRUBA2")
        cursor= conn.cursor()

        cursor.execute("""
            SELECT * FROM Nombre1
        """)
        
        rows= cursor.fetchall()
        
        result = "<table class='table table-hover'>"
        result += "<tr><th>PEDRO</th><th>CRIZ</th> </tr>"

        for row in rows:
             result += "<tr><td>" + str(row[0])  + "</td>"
             result += "<td> " + str(row[1])+ "</td> </tr>"

        result += "</table>"    

        conn.close()
        print("Conecion exitosa :D")

        return HTMLResponse(content=headerMOvies + result + footer_html, status_code=200)
        
    except mysql.connector.Error as eror :
         
         return {}

@user.get("/InsertarPagina")
async def InsercionMask():
    hmtCOnus = """"
        <!doctype html>
<html lang='en'>
  <head>
    <meta charset='utf-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <title>PLANTILLA</title>
    <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH' crossorigin='anonymous'>
    <link rel="stylesheet" href="static/css/styles.css">
  </head>
  <body>
    <div class='container mt-5'>
      <div class='d-flex align-items-center mb-4'>

        <img src='static/images/logo.png' alt='bot' class='logo'>
      
        <div class='title-container ms-3'>
          <h1>Resultados de la Consulta SQL</h1>
        </div>
      </div>
      <div class="form-container">  <!-- Agregamos la clase form-container al contenedor del formulario -->
        <h1>Insertar Datos en la Base de Datos</h1> 
        <form action="/insertDB" method="post">
          <label for="op1">Valor de Op1:</label>
          <input type="text" id="op1" name="Op1"><br><br>
          <label for="op2">Valor de Op2:</label>
          <input type="text" id="op2" name="Op2"><br><br>
          <input type="submit" value="Insertar Datos">
        </form>
      </div>
    </div>  

    <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js' integrity='sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz' crossorigin='anonymous'></script>
  </body>
</html>
    
    """


    return HTMLResponse(hmtCOnus, status_code=200)
        
    
@user.post("/insertDB")
async def InsertarDatos(request: Request, Op1: str = Form(...), Op2: str = Form(...)):


    try:
        conn = create_connection("localhost","root","root", "PRUBA2")
        cursor = conn.cursor()
        print("Conecion exitosa :D2222")
        cursor.execute(f"""
            INSERT INTO `Nombre1`(`Pedro`, `Cruz`) VALUES (%s, %s)
        """, (Op1, Op2))

        conn.commit()
        conn.close()
        
        return HTMLResponse(content=f" INSERT EXITOSO :D DATOS {Op1},{Op2}", status_code=200)

    except Error as error:
        #return {}
        raise HTTPException(status_code=500, detail=f"Error al insertar datos: {error}")


