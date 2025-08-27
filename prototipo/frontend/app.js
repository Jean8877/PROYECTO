// Definir una constante global para la URL base
const BASE_URL = "http://127.0.0.1:5000/";

// Función para visualizar datos en la tabla
function visualizar(data) {
    let tabla = ""; // Inicializa la variable para almacenar el HTML de la tabla

    // Recorre cada elemento en el array "baul" y crea una fila de tabla
    data.baul.forEach(item => {
        tabla += `
            <tr data-id="${item.id_baul}">
                <td>${item.id_baul}</td>
                <td>${item.plataforma}</td>
                <td>${item.usuario}</td>
                <td>${item.clave}</td>
                <td>
                    <!-- Botón para editar -->
                    <button type='button' class='btn btn-info'
                        onclick="location.href = 'edit.html?variable1=${item.id_baul}'">
                        <img src="imagenes/edit.png" height='30' width='30'/>
                    </button>
                </td>
                <td>
                    <!-- Botón para eliminar -->
                    <button type='button' class='btn btn-warning'
                        onclick="eliminar(${item.id_baul})">
                        <img src="imagenes/delete.png" height='30' width='30'/>
                    </button>
                    </td>
                </tr>`;
    });

    // Inserta las filas generadas en el cuerpo de la tabla
    document.getElementById('data').innerHTML = tabla;
}

// funcion para realizar una consulta general
function consulta_general() {
    fetch(`${BASE_URL}/`) // Realiza una solicitud GET al endpoint
        .then(response => {
            if (!response.ok) throw new Error(`Error: ${response.status}`); // manejo errores HTTP
            return response.json();
        })
        .then(data => visualizar(data)) // muestra los datos en la tabla
        .catch(error => console.error('Error:', error)); // captura y muestra errores en la consola
}

// funcion para eliminar u registro (DELETE)
function eliminar(id) {
    fetch(`${BASE_URL}/eliminar/${id}`, { method: 'DELETE'}) // Solucitud DELETE
        .then(response => {
            if (!response.ok) throw new Error(`Error: ${response.status}`); // manejo de errores HTTP
            return  response.json();
        })
        .then(res => {
            actualizarDOM(id); // elimina el elemento directamente del DOM
            swal("mesaje", `Registro ${res.mesaje} exitosamente`, "success"); // notificacion de éxito
        })
        .catch(error => console.error('Error:', error)); // captura y muestra errores en la consola
}

// funcion para actualizar el DOM despues de eliminar un elemento
function actualizarDOM(id) {
    const row = document.querySelector(`tr[data-id="${id}"]`);
    if (row) row.remove(); // Elimina directamente la fija del DOM
}

// Funcion para registrar nuevos regiistro (POST)
function registrar() {
    //obtiene los valores de los campos de entrada
    const plat =document.getElementById("plataforma").value;
    const usua =document.getElementById("usuario").value;
    const clav =document.getElementById("clave").value;

    // crea EL OBJETO De DATOS
    const data = {
        plataforma:plat,
        usuario: usua,
        clave: clav
    };

    // console.log(data); // Mostrar datos para depuración

    fetch(`${BASE_URL}/registro/`, {
        method: "POST", // Método HTTP POST para registrar
        body: JSON.stringify(data), // Convierte el objeto a JSON
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => {
        if (!response.ok) throw new Error(`Error: ${response.status}`);
        return response.json();
    })
    .then(response => {
        if (response.mensaje === "Error") {
            swal("Mensaje", "Error en el registro", "error"); // Alerta de error
        } else {
            consulta_general(); // Refresca la tabla de datos sin recargar la página
            swal("Mensaje", "Registro agregado exitosamente", "success"); // Alerta de éxito
        }
    })
    .catch(error => console.error('Error:', error)); // Captura errores
}

// Función para consultar un registro individual (GET)
function consulta_individual(id) {
    fetch(`${BASE_URL}/consulta_individual/${id}`) // Solicitud GET al endpoint
        .then(response => {
            if (!response.ok) throw new Error(`Error: ${response.status}`);
            return response.json(); // Convierte la respuesta en JSON
        })
        .then(data => {
            // console.log(data); // Mostrar datos para depuración
            // Rellena los campos de entrada con los valores obtenidos
            document.getElementById("plataforma").value = data.baul.Plataforma;
            document.getElementById("usuario").value = data.baul.usuario;
            document.getElementById("clave").value = data.baul.clave;
        })
        .catch(error => console.error('Error:', error)); // Captura errores
}

// Función para modificar un registro existente (PUT)
function modificar(id) {
    // Obtiene los valores de los campos de entrada
    const plat = document.getElementById("plataforma").value;
    const usua = document.getElementById("usuario").value;
    const clav = document.getElementById("clave").value;

    // Crea el objeto de datos
    const data = {
        plataforma: plat,
        usuario: usua,
        clave: clav
    };

    // console.log(data); // Mostrar datos para depuración

    fetch(`${BASE_URL}/actualizar/${id}`, {
        method: "PUT", // Método HTTP PUT para actualizar
        body: JSON.stringify(data), // Convierte el objeto a JSON
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => {
        if (!response.ok) throw new Error(`Error: ${response.status}`);
        return response.json();
    })
    .then(response => {
        if (response.mensaje === "Error") {
            swal("Mensaje", "Error al actualizar el registro", "error"); // Alerta de error
        } else {
            consulta_general(); // Refresca la tabla de datos sin recargar la página
            swal("Mensaje", "Registro actualizado exitosamente", "success"); // Alerta de éxito
        }
    })
    .catch(error => console.error('Error:', error)); // Captura errores
}