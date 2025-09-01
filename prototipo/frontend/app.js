const BASE_URL = "http://127.0.0.1:5000";

// Funcion para realizar una consulta general (GET)
function tipo_usuario() {
    fetch(`${BASE_URL}/tipo_usuario`)
        .then(response => {
            if (!response.ok) throw new Error(`Error: ${response.status}`); // Manejo de errores HTTP
            console.log(response)
            return response.json();
        })
        .then( data => visualizar(data)) // Muestra los datos en la tabla
        .catch(error => console.error('Error:', error)); // Captura y muestra los errores en la pantalla
}