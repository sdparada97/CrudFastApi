# CrudFastApi

Esta APIRest esta construida con FastApi y MongoDB, todo el ambiente esta contenerizado en Docker.

<table>
   <tr>
       <td>
           <img src="https://d1.awsstatic.com/acs/characters/Logos/Docker-Logo_Horizontel_279x131.b8a5c41e56b77706656d61080f6a0217a3ba356d.png" width="300" height="200" border="10"/>
       </td>
       <td>
           <img src="https://repository-images.githubusercontent.com/260928305/92388600-8d1c-11ea-9993-a726466b5099" width="300" height="200" border="10"/>
       </td>
       <td>
           <img src="https://i.blogs.es/577c8b/650_1000_mongo_bumper.sh-600x600/1366_2000.png"  width="200" height="200" border="10"/>
       </td>
   </tr>
</table>


## Instrucciones
> 1. Clonar repositorio
>
>    `git clone https://github.com/sdparada97/CrudFastApi.git`
>
> 2. Realice la dockerización del proyecto
>
>     `docker-compose up --build`
>
> 3. Ir al navegador a la ruta:
>
>     `http://localhost:8989/docs`
>
> 4. APIs REST:
>     - Usuario Routes:
>
>         **GET**
>         > `/users`
>
>         **POST**
>         >`/users`
>
>         **GET**
>         > `/users/{id}`
>
>         **PUT**
>         >`/users/{id}`
>
>         **DELETE**
>         >`/users/{id}`
>
>     - Vacante Routes:
>
>         **GET**
>         > `/vacancies`
>
>         **POST**
>         >`/vacancies`
>
>         **GET**
>         >`/vacancies/{id}`
>
>         **PUT**
>         >`/vacancies/{id}`
>
>         **DELETE**
>         >`/vacancies/{id}`

## Evidencias

### Swagger API-REST

### VScode Dockerizado