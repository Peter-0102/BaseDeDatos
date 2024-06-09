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
            <input type="password" id='password' name='PassWord'>
            
            
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
        return RedirectResponse(url="/menuA",status_code=303)
    elif(User == "User" and PassWord =="123"):   
        return RedirectResponse(url="/menuU",status_code=303)
    else:
        print("user no admin no normal")
        return RedirectResponse(url="/", status_code=303)




@user.get("/menuU")
async def menuU():
    html_content="""
 <!doctype html>
<html lang='en'>
<head>
  <meta charset='utf-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1'>
  <title>CINESTREAM</title>
  <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH' crossorigin='anonymous'>
  <link rel='stylesheet' href='static/css/styles3.css'>
</head>
<body>
<nav class='navbar navbar-expand-lg bg-body-tertiary'>
  <div class='container-fluid'>
    <a class='navbar-brand' href='#'>CINESTREAM</a>
    <button class='navbar-toggler' type='button' data-bs-toggle='collapse' data-bs-target='#navbarSupportedContent' aria-controls='navbarSupportedContent' aria-expanded='false' aria-label='Toggle navigation'>
      <span class='navbar-toggler-icon'></span>
    </button>
    <div class='collapse navbar-collapse' id='navbarSupportedContent'>
      <ul class='navbar-nav me-auto mb-2 mb-lg-0'>
        <li class='nav-item dropdown'>
          <a class='nav-link dropdown-toggle' href='#' role='button' data-bs-toggle='dropdown' aria-expanded='false'>
            PELICULAS
          </a>
          <ul class='dropdown-menu'>
            <li><hr class='dropdown-divider'></li>
            <li>
              <form action= '/ConsultaPeli' method='post' class='dropdown-item p-2'>
                <input class='form-control' type='text'  id = 'titulo' name ='Titulo'   placeholder='Search' aria-label='Search' >
              </form>
            </li>
          </ul>
        </li>
        <li class='nav-item dropdown'>
          <a class='nav-link dropdown-toggle' href='#' role='button' data-bs-toggle='dropdown' aria-expanded='false'>
            PRODUCTORA
          </a>
          <ul class='dropdown-menu'>
            <li><hr class='dropdown-divider'></li>
            <li>
              <form action= '/ConsultaProductora' method='post' class='dropdown-item p-2'>
                
                <input class='form-control' type='text'  id = 'productora' name='Productora'   placeholder='Search' aria-label='Search' >
              </form>
            </li>
          </ul>
        </li>
        <li class='nav-item dropdown'>
          <a class='nav-link dropdown-toggle' href='#' role='button' data-bs-toggle='dropdown' aria-expanded='false'>
            GENERO
          </a>
          <ul class='dropdown-menu'>
            <li><hr class='dropdown-divider'></li>
            <li>
              <form action= '/ConsultaGenero' method='post' class='dropdown-item p-2'>
                <input class='form-control' type='text'  id = 'genero' name ='Genero'   placeholder='Search' aria-label='Search' >
              </form>
            </li>
          </ul>
        </li>
        <li class='nav-item dropdown'>
          <a class='nav-link dropdown-toggle' href='#' role='button' data-bs-toggle='dropdown' aria-expanded='false'>
            DOBLAJE
          </a>
          <ul class='dropdown-menu'>
            <li><hr class='dropdown-divider'></li>
            <li>
              <form action= '/ConsultaDoblaje' method='post' class='dropdown-item p-2'>
                <input class='form-control' type='text'  id = 'doblaje' name ='Doblaje'   placeholder='Search' aria-label='Search' >
              </form>
            </li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</nav>
<div id=carousel1>
  <div id='carouselExampleIndicators' class='carousel slide' data-bs-ride='carousel'>
  <div class='carousel-inner'>
    <div class='carousel-item active'>
      <div class='d-flex justify-content-between'>
        <img src='static/images/imagen1.jpeg' alt='...' class='d-block '>
        <img src='static/images/imagen2.webp' alt='...' class='d-block '>
        <img src='static/images/imagen3.jpg' alt='...' class='d-block '>
        <img src='static/images/imagen4.jpg' alt='...' class='d-block '>
        <img src='static/images/imagen5.jpg' alt='...' class='d-block '>
        <img src='static/images/imajen6.jpg' alt='...' class='d-block '>
      </div>
    </div>
    <div class='carousel-item'>
      <div class='d-flex justify-content-between'>
        <img src='static/images/imagen1.jpeg' alt='...' class='d-block '>
        <img src='static/images/imagen2.webp' alt='...' class='d-block '>
        <img src='static/images/imagen3.jpg' alt='...' class='d-block '>
        <img src='static/images/imagen4.jpg' alt='...' class='d-block '>
        <img src='static/images/imagen5.jpg' alt='...' class='d-block '>
        <img src='static/images/imajen6.jpg' alt='...' class='d-block '>
      </div>
    </div>
  </div>
  <button class='carousel-control-prev' type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide='prev'>
    <span class='carousel-control-prev-icon' aria-hidden='true'></span>
    <span class='visually-hidden'>Previous</span>
  </button>
  <button class='carousel-control-next' type='button' data-bs-target='#carouselExampleIndicators' data-bs-slide='next'>
    <span class='carousel-control-next-icon' aria-hidden='true'></span>
    <span class='visually-hidden'>Next</span>
  </button>
</div>
</div>
<div class='images-container'>
  <img src='static/images/imagen3.jpg' alt='Imagen 1'>
  <img src='static/images/imagen4.jpg' alt='Imagen 2'>
  <img src='static/images/imagen5.jpg' alt='Imagen 3'>
  <img src='static/images/imajen6.jpg' alt='Imagen 4'>
  <img src='static/images/imagen7.jpg' alt='Imagen 5'>
  <img src='static/images/imagen3.jpg' alt='Imagen 1'>
  <img src='static/images/imagen4.jpg' alt='Imagen 2'>
  <img src='static/images/imagen5.jpg' alt='Imagen 3'>
  <img src='static/images/imajen6.jpg' alt='Imagen 4'>
  <img src='static/images/imagen7.jpg' alt='Imagen 5'>
  <img src='static/images/imagen3.jpg' alt='Imagen 1'>
  <img src='static/images/imagen4.jpg' alt='Imagen 2'>
  <img src='static/images/imagen5.jpg' alt='Imagen 3'>
  <img src='static/images/imajen6.jpg' alt='Imagen 4'>
  <img src='static/images/imagen7.jpg' alt='Imagen 5'>
  <img src='static/images/imagen3.jpg' alt='Imagen 1'>
  <img src='static/images/imagen4.jpg' alt='Imagen 2'>
  <img src='static/images/imagen5.jpg' alt='Imagen 3'>
  <img src='static/images/imajen6.jpg' alt='Imagen 4'>
</div>
    <!-- Al final del body de tu documento HTML -->
    <script src='https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js'></script>

    <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js' integrity='sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz' crossorigin='anonymous'></script>
  </body>
  <script>
  // Inicializa el carrusel
  var myCarousel = document.querySelector('#carouselExampleSlidesOnly');
  var carousel = new bootstrap.Carousel(myCarousel);
</script>
</html>
     """
    return HTMLResponse(content=html_content, status_code=200)


@user.post("/ConsultaPeli")

async def ConsultaPeliculas(request: Request, Titulo: str = Form(...)):
    # Encabezado HTML con Bootstrap
    headerMovies = """
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Consulta de Películas</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
            <style>
                body {
                    background-color: #f8f9fa;
                }
                .container {
                    margin-top: 50px;
                }
                .table th, .table td {
                    vertical-align: middle;
                }
                .mi-boton {
                    display: inline-block;
                    padding: 10px 20px;
                    background-color: #007bff;
                    color: #fff;
                    text-decoration: none;
                    border-radius: 5px;
                }
                .mi-boton:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1 class="mb-4">Consulta de Películas</h1>
    """

    # Conexión a la base de datos
    print(Titulo)
    conn = create_connection("localhost", "root", "root", "movies")

    cursor = conn.cursor()

    # Ejecutar consulta SQL
    cursor.execute(f"""SELECT title, overview, ROUND(popularity, 2), release_date, vote_average 
                       FROM movie 
                       WHERE title LIKE '%{Titulo}%' 
                       LIMIT 5;""")
    
    rows = cursor.fetchall()

    # Generar tabla HTML con los resultados
    result = """
                <div class="table-responsive">
                    <table class="table table-hover">
                        <thead>
                            <tr>
                                <th>IMAGEN</th>
                                <th>TÍTULO</th>
                                <th>SINOPSIS</th>
                                <th>POPULARIDAD</th>
                                <th>LANZAMIENTO</th>
                                <th>APROBACIÓN</th>
                            </tr>
                        </thead>
                        <tbody>
    """
    for row in rows:
        result += f"""
                            <tr>
                                <td><img src="static/images/imagen5.jpg" alt="Imagen 3" style="width: 100px; height: 100px;"></td>
                                <td>{row[0]}</td>
                                <td>{row[1]}</td>
                                <td>{row[2]}</td>
                                <td>{row[3]}</td>
                                <td>{row[4]}</td>
                            </tr>
        """
    result += """
                        </tbody>
                    </table>
                </div>
            </div>
        </body>
        </html>
    """
    result +="""
    <div class="text-center"> <!-- Div centrado -->
        <a href="/menuU" class="mi-boton">Regresar menu</a>
    </div>
    """
    # Cerrar conexión a la base de datos
    conn.close()

    # Devolver respuesta HTML
    return HTMLResponse(content=headerMovies + result, status_code=200)


@user.post("/ConsultaGenero")
async def ConsulaGenero(request: Request, Genero: str = Form(...)):
  
    headerMovies = """
        <!doctype html>
        <html lang='en'>
          <head>
          <meta charset='utf-8'>
          <meta name='viewport' content='width=device-width, initial-scale=1'>
          <title>Consulta de Género</title>
          <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH' crossorigin='anonymous'>
          
          <style>
              body {
                  background-color: white; /* Establece el fondo en blanco */
              }
          </style>
          </head>
          <body>
            <div class="container">
    """

    conn = create_connection("localhost", "root", "root", "movies")
    cursor = conn.cursor()

    cursor.execute(f"""SELECT M.title
                        FROM movie as M
                        LEFT JOIN movie_genres on movie_genres.movie_id = M.movie_id
                        LEFT JOIN genre on genre.genre_id = movie_genres.genre_id
                        WHERE genre.genre_name like '%{Genero}%'
                        limit 20;""")

    result = "<table class='table table-hover'>"
    result += "<tr><th>IMAGEN</th><th>TITULO</th></tr>"

    rows = cursor.fetchall() 

    for row in rows:
        result += "<tr>"
        result += "<td><img src='static/images/imagen5.jpg' alt='Imagen 3' style='width: 100px; height: 100px;'></td>"
        result += "<td>" + str(row[0]) + "</td>"
        result += "</tr>"

    result += "</table>"  
    result += '<a href="/menuU" class="btn btn-primary">Volver al Menú</a>'

    conn.commit()
    conn.close()

    footer_html = """
        </div> <!-- Cierre del contenedor "container" -->
        </body>
        </html>
    """

    return HTMLResponse(content=headerMovies + result + footer_html, status_code=200)

@user.post("/ConsultaProductora")
async def ConsultaProductora(request: Request, Productora: str = Form(...)):

    # Encabezado HTML con Bootstrap
    headerMovies = """
        <!DOCTYPE html>
        <html lang='es'>
            <head>
                <meta charset='UTF-8'>
                <meta name='viewport' content='width=device-width, initial-scale=1.0'>
                <title>Consulta de Productora</title>
                <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet'>
            </head>
            <body>
                <div class="container">
    """

    # Conexión a la base de datos
    conn = create_connection("localhost", "root", "root", "movies")
    cursor = conn.cursor()

    # Ejecutar consulta SQL
    cursor.execute(f"""SELECT movie.title, production_company.company_name
                       FROM movie
                       LEFT JOIN movie_company ON movie.movie_id = movie_company.movie_id
                       LEFT JOIN production_company ON movie_company.company_id = production_company.company_id
                       WHERE production_company.company_name LIKE '%{Productora}%';""")

    # Generar tabla HTML con los resultados
    result = "<table class='table table-hover'>"
    result += "<tr><th>IMAGEN</th><th>Título</th><th>Productora</th></tr>"

    rows = cursor.fetchall() 

    for row in rows:
        result += "<tr>"
        result += "<td><img src='static/images/imagen5.jpg' alt='Imagen 3' style='width: 100px; height: 100px;'></td>"
        result += "<td>" + str(row[0]) + "</td>"
        result += "<td>" + str(row[1]) + "</td>"
        result += "</tr>"

    result += "</table>"  

    # Cerrar conexión a la base de datos
    conn.commit()
    conn.close()

    # Enlace para volver al menú
    volver_menu = '<a href="/menuU" class="btn btn-primary">Volver al Menú</a>'

    # Pie de página HTML
    footer_html = """
                </div> <!-- Cierre del contenedor "container" -->
            </body>
        </html>
    """

    # Devolver respuesta HTML
    return HTMLResponse(content=headerMovies + result + volver_menu + footer_html, status_code=200)

@user.post("/ConsultaDoblaje")
async def ConsultaDoblaje(request: Request, Doblaje: str = Form(...)):
  headerMovies = """
        <!DOCTYPE html>
        <html lang='es'>
            <head>
                <meta charset='UTF-8'>
                <meta name='viewport' content='width=device-width, initial-scale=1.0'>
                <title>Consulta de Doblaje</title>
                <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet'>
                
            </head>
            <body>
                <div class="container">
    """

    # Conexión a la base de datos
  conn = create_connection("localhost", "root", "root", "movies")
  cursor = conn.cursor()

    # Ejecutar consulta SQL
  cursor.execute(f"""SELECT movie.title, language.language_name
                       FROM movie
                       LEFT JOIN movie_languages ON movie.movie_id = movie_languages.movie_id
                       LEFT JOIN language ON movie_languages.language_id = language.language_id
                       WHERE language.language_name LIKE '%{Doblaje}%';""")

    # Título con el idioma de doblaje
  result = f"<h2>Películas dobladas a '{Doblaje}'</h2>"

    # Generar tabla HTML con los resultados
  result += "<table class='table table-hover'>"
  result += "<tr><th>IMAGEN</th><th>Título</th><th>Idioma</th></tr>"

  rows = cursor.fetchall() 

  for row in rows:
      result += "<tr>"
      result += "<td><img src='static/images/imagen5.jpg' alt='Imagen 3' style='width: 100px; height: 100px;'></td>"
      result += "<td>" + str(row[0]) + "</td>"
      result += "<td>" + str(row[1]) + "</td>"
      result += "</tr>"

  result += "</table>"  

  # Cerrar conexión a la base de datos
  conn.commit()
  conn.close()

  # Enlace para volver al menú
  volver_menu = '<a href="/menuU" class="btn btn-primary">Volver al Menú</a>'

  # Pie de página HTML
  footer_html = """
              </div> <!-- Cierre del contenedor "container" -->
          </body>
      </html>
  """

  # Devolver respuesta HTML
  return HTMLResponse(content=headerMovies + result + volver_menu + footer_html, status_code=200)








@user.get("/menuA")
async def menuA():
    html_content="""
   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>admin</title>
    <link rel="stylesheet" href="static/css/styles4.css">
</head>
<body>
   <h1>Menú admin</h1>
    <ul>
        <li class="dropdown">
            <a href="#">Agregar</a>
            <ul class="dropdown-menu">
                <li><a href="/InsertarActor">Agregar Actor</a></li>
                <li><a href="/InsertarPelicula">Agregar Pelicula</a></li>
                <li><a href="/InsertarKeyWord">Agregar keyword</a></li>
            </ul>
        </li>
        <li><a href="#">Eliminar</a></li>
        <li><a href="#">Actualizar</a></li>
    </ul>
</body>
</html>

     """
    return HTMLResponse(content=html_content, status_code=200)



@user.get("/InsertarActor")
async def InsertarActor(request: Request, message: str = None, error: str = None):
    hmtCOnus = f"""
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
                        <h1>Insertar nuevo actor</h1>
                    </div>
                </div>
                <div class="form-container">
                    {f"<div class='alert alert-success'>{message}</div>" if message else ""}
                    {f"<div class='alert alert-danger'>{error}</div>" if error else ""}
                    <form action="/insertActor" method="post">
                        <label for="op1">Nuevo ID :</label>
                        <input type="text" id="op1" name="person_id"><br><br>
                        <label for="op2">Nombre :</label>
                        <input type="text" id="op2" name="person_name"><br><br>
                        <input type="submit" value="Insertar Datos">
                    </form>
                </div>
                <a href="/menuA" class="btn btn-primary">Volver al Menú</a>
            </div>
            <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js' integrity='sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz' crossorigin='anonymous'></script>
        </body>
        </html>
    """
    return HTMLResponse(hmtCOnus, status_code=200)

@user.post("/insertActor")
async def InsertarDatos(request: Request, person_id: str = Form(...), person_name: str = Form(...)):
    try:
        conn = create_connection("localhost", "root", "root", "movies")
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO person (person_id, person_name) VALUES (%s, %s)
        """, (person_id, person_name))
        
        conn.commit()
        conn.close()
        
        return RedirectResponse(url=f"/InsertarActor?message=Insertar+Exitoso%3A+{person_id}%2C+{person_name}", status_code=303)

    except Error as error:
        return RedirectResponse(url=f"/InsertarActor?error=Error+al+insertar+datos%3A+{str(error)}", status_code=303)


@user.get("/InsertarPelicula")
async def InsertarPelicula(request: Request, message: str = None, error: str = None):
    hmtCOnus = f"""
        <!doctype html>
        <html lang='en'>
        <head>
            <meta charset='utf-8'>
            <meta name='viewport' content='width=device-width, initial-scale=1'>
            <title>Insertar Nueva Película</title>
            <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH' crossorigin='anonymous'>
            <link rel="stylesheet" href="static/css/styles.css">
        </head>
        <body>
            <div class='container mt-5'>
                <div class='d-flex align-items-center mb-4'>
                    <img src='static/images/logo.png' alt='bot' class='logo'>
                    <div class='title-container ms-3'>
                        <h1>Insertar Nueva Película</h1>
                    </div>
                </div>
                <div class="form-container">
                    {f"<div class='alert alert-success'>{message}</div>" if message else ""}
                    {f"<div class='alert alert-danger'>{error}</div>" if error else ""}
                    <form action="/insertPelicula" method="post">
                        <label for="id_pelicula">ID Película:</label>
                        <input type="text" id="id_pelicula" name="id_pelicula"><br><br>
                        <label for="title">Título:</label>
                        <input type="text" id="title" name="title"><br><br>
                        <label for="budget">Presupuesto:</label>
                        <input type="text" id="budget" name="budget"><br><br>
                        <label for="homepage">Página Principal:</label>
                        <input type="text" id="homepage" name="homepage"><br><br>
                        <label for="overview">Resumen:</label>
                        <input type="text" id="overview" name="overview"><br><br>
                        <label for="popularity">Popularidad:</label>
                        <input type="text" id="popularity" name="popularity"><br><br>
                        <label for="release_date">Fecha de Estreno:</label>
                        <input type="text" id="release_date" name="release_date"><br><br>
                        <label for="revenue">Ingresos:</label>
                        <input type="text" id="revenue" name="revenue"><br><br>
                        <label for="runtime">Duración:</label>
                        <input type="text" id="runtime" name="runtime"><br><br>
                        <label for="movie_status">Estado:</label>
                        <input type="text" id="movie_status" name="movie_status"><br><br>
                        <label for="tagline">Eslogan:</label>
                        <input type="text" id="tagline" name="tagline"><br><br>
                        <label for="vote_average">Promedio de Votos:</label>
                        <input type="text" id="vote_average" name="vote_average"><br><br>
                        <label for="vote_count">Número de Votos:</label>
                        <input type="text" id="vote_count" name="vote_count"><br><br>
                        <input type="submit" value="Insertar Película">
                    </form>
                </div>
                <a href="/menuA" class="btn btn-primary">Volver al Menú</a>
            </div>
            <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js' integrity='sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz' crossorigin='anonymous'></script>
        </body>
        </html>
    """
    return HTMLResponse(hmtCOnus, status_code=200)

@user.post("/insertPelicula")
async def insertPelicula(request: Request, id_pelicula: str = Form(...), title: str = Form(...),
                          budget: str = Form(...), homepage: str = Form(...), overview: str = Form(...),
                          popularity: str = Form(...), release_date: str = Form(...), revenue: str = Form(...),
                          runtime: str = Form(...), movie_status: str = Form(...), tagline: str = Form(...),
                          vote_average: str = Form(...), vote_count: str = Form(...)):
    try:
        conn = create_connection("localhost", "root", "root", "movies")
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO movie ( id_pelicula, title, budget, homepage, overview, popularity, release_date, revenue, runtime, movie_status, tagline, vote_average, vote_count)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, ( id_pelicula, title, budget, homepage, overview, popularity, release_date, revenue, runtime, movie_status, tagline, vote_average, vote_count))
        
        conn.commit()
        conn.close()
        
        return RedirectResponse(url=f"/InsertarPelicula?message=Insertar+Exitoso%3A+{title}", status_code=303)

    except Error as error:
        return RedirectResponse(url=f"/InsertarPelicula?error=Error+al+insertar+datos%3A+{str(error)}", status_code=303)
    

@user.get("/InsertarKeyWord")
async def InsertarKeyWord(request: Request, message: str = None, error: str = None):
    hmtCOnus = f"""
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
                        <h1>Insertar nuevo actor</h1>
                    </div>
                </div>
                <div class="form-container">
                    {f"<div class='alert alert-success'>{message}</div>" if message else ""}
                    {f"<div class='alert alert-danger'>{error}</div>" if error else ""}
                    <form action="/insertKeyWord" method="post">
                        <label for="op1">Nuevo ID :</label>
                        <input type="text" id="op1" name="id_keyword"><br><br>
                        <label for="op2">KeyWord :</label>
                        <input type="text" id="op2" name="keyword"><br><br>
                        <input type="submit" value="Insertar Datos">
                    </form>
                </div>
                <a href="/menuA" class="btn btn-primary">Volver al Menú</a>
            </div>
            <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js' integrity='sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz' crossorigin='anonymous'></script>
        </body>
        </html>
    """
    return HTMLResponse(hmtCOnus, status_code=200)

@user.post("/insertKeyWord")
async def insertKeyWord(request: Request, id_keyword: str = Form(...), keyword: str = Form(...)):
    try:
        conn = create_connection("localhost", "root", "root", "movies")
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO keyword(`keyword_id`, `keyword_name`) VALUES (%s,%s)                       
        """, (id_keyword, keyword))
        
        conn.commit()
        conn.close()
        
        return RedirectResponse(url=f"/InsertarActor?message=Insertar+Exitoso%3A+{id_keyword}%2C+{keyword}", status_code=303)

    except Error as error:
        return RedirectResponse(url=f"/InsertarActor?error=Error+al+insertar+datos%3A+{str(error)}", status_code=303)
