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

@user.get("/")
async def read_root():
	html_content = header_html + """
     
     <!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <!-- Title Page -->  
    <title>Login</title>
 
    <!-- CSS -->
    <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH' crossorigin='anonymous'>
    <link rel="stylesheet" href="static/css/styles2.css">
    
</head>
<body>
    <div id="container2"></div>
    <div id="container">
        <form action= '/Login' method = 'post'>
            <!-- Username --> 
            <p>CINESTREAM</p>
            
            <label for='user'>Username: </label>
            <input type="text" id='user' name='User'>
            <!-- Password -->
            
            <label for="password">Password:</label>
            <input type="text" id='password' name='PassWord'>
            
            
                <!-- Submit Button -->
                <input type="submit" value="Login">
            </div>
        </form>       
    </div>
</body>
</html>""" + footer_html
    
	return HTMLResponse(content=html_content, status_code=200)


@user.post("/Login")
async def InicioSecion(request: Request, User: str = Form(...), PassWord: str= Form(...)):
    print(User)
    print(PassWord)
    if ( User == "root" and PassWord == "root"):
        return RedirectResponse(url="/InsertarPagina",status_code=303)
    elif(User == "User" and PassWord =="123"):   
        return RedirectResponse(url="/movies",status_code=303)
    else:
        print("user no admin no normal")
        return RedirectResponse(url="/", status_code=303)




@user.get("/menuU")
async def menuU():
    html_content="""
     <!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="static/css/styles3.css">
    
  </head>
  <body>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" aria-disabled="true">Disabled</a>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>

<div id=carousel1>
  <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <div class="d-flex justify-content-between">
        <img src="static/images/imagen1.jpeg" alt="..." class="d-block ">
        <img src="static/images/imagen2.webp" alt="..." class="d-block ">
        <img src="static/images/imagen3.jpg" alt="..." class="d-block ">
        <img src="static/images/imagen4.jpg" alt="..." class="d-block ">
        <img src="static/images/imagen5.jpg" alt="..." class="d-block ">
        <img src="static/images/imajen6.jpg" alt="..." class="d-block ">
      </div>
    </div>
    <div class="carousel-item">
      <div class="d-flex justify-content-between">
        <img src="static/images/imagen1.jpeg" alt="..." class="d-block ">
        <img src="static/images/imagen2.webp" alt="..." class="d-block ">
        <img src="static/images/imagen3.jpg" alt="..." class="d-block ">
        <img src="static/images/imagen4.jpg" alt="..." class="d-block ">
        <img src="static/images/imagen5.jpg" alt="..." class="d-block ">
        <img src="static/images/imajen6.jpg" alt="..." class="d-block ">
      </div>
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
</div>
<div class="images-container">
  <img src="static/images/imagen3.jpg" alt="Imagen 1">
  <img src="static/images/imagen4.jpg" alt="Imagen 2">
  <img src="static/images/imagen5.jpg" alt="Imagen 3">
  <img src="static/images/imajen6.jpg" alt="Imagen 4">
  <img src="static/images/imagen7.jpg" alt="Imagen 5">
</div>
    <!-- Al final del body de tu documento HTML -->
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
  <script>
  // Inicializa el carrusel
  var myCarousel = document.querySelector('#carouselExampleSlidesOnly');
  var carousel = new bootstrap.Carousel(myCarousel);
</script>
</html>
     
     """
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


