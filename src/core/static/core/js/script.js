document.addEventListener('DOMContentLoaded', function () {
    const carrito = document.getElementById('carrito');
    const lista = document.querySelector('#lista-carrito tbody');
    const vaciarCarritoBtn = document.getElementById('vaciar-carrito');
    const comprarcarritoBtn = document.getElementById('Comprar-carrito');

    cargarEventlisteners();
    configurarIdProductos();
    leerLocalStorage();

    function cargarEventlisteners() {
        const elementosAgregarCarrito = document.querySelectorAll('.agregar-carrito');
        elementosAgregarCarrito.forEach((elemento) => {
            elemento.addEventListener('click', comprarElemento);
        });

        if (carrito) {
            carrito.addEventListener('click', eliminarElemento);
        }
        if (vaciarCarritoBtn) {
            vaciarCarritoBtn.addEventListener('click', vaciarCarrito);
        }
        if (comprarcarritoBtn) {
            comprarcarritoBtn.addEventListener('click', comprarcarrito);
        }
    }

    function comprarElemento(e) {
        e.preventDefault();
        if (e.target.classList.contains('agregar-carrito')) {
            const elemento = e.target.parentElement.parentElement;
            leerDatosElemento(elemento);
        }
    }

    function leerDatosElemento(elemento) {
        const infoElemento = {
            imagen: elemento.querySelector('img').src,
            titulo: elemento.querySelector('h3').textContent,
            precio: elemento.querySelector('.precio').textContent,
            id: elemento.querySelector('.agregar-carrito').getAttribute('data-id'),
            cantidad: 1
        };

        let elementosLS = obtenerProductosLocalStorage();
        const productoExistente = elementosLS.some(producto => producto.id === infoElemento.id);
        if (!productoExistente) {
            insertarCarrito(infoElemento);
            guardarProductosLocalStorage(infoElemento);
        }
    }

    function insertarCarrito(elemento) {
        if (lista) {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>
                    <img src="${elemento.imagen}" width="100">
                </td>
                <td>
                    ${elemento.titulo}
                </td>
                <td>
                    ${elemento.precio}
                </td>
                <td>
                    <a href="#" class="borrar" data-id="${elemento.id}">X</a>
                </td>
            `;
            lista.appendChild(row);
        } else {
            console.error('El elemento lista no se encuentra en el DOM');
        }
    }

    function configurarIdProductos() {
        const productosTel = document.querySelectorAll("[data-id]");
        let contador = 0;
        productosTel.forEach(el => {
            el.setAttribute('data-id', contador);
            contador++;
        });
    }

    function eliminarElemento(e) {
        e.preventDefault();
        let elemento, elementoID;
        if (e.target.classList.contains('borrar')) {
            elemento = e.target.parentElement.parentElement;
            elementoID = e.target.getAttribute('data-id');
            elemento.remove();

            eliminarProductosLocalStorage(elementoID);
        }
    }

    function vaciarCarrito() {
        while (lista && lista.firstChild) {
            lista.removeChild(lista.firstChild);
        }
        localStorage.removeItem('elementos');
        return false;
    }

    function guardarProductosLocalStorage(elemento) {
        let elementos = obtenerProductosLocalStorage();
        elementos.push(elemento);
        localStorage.setItem('elementos', JSON.stringify(elementos));
    }

    function obtenerProductosLocalStorage() {
        let elementoLS;
        if (localStorage.getItem('elementos') === null) {
            elementoLS = [];
        } else {
            elementoLS = JSON.parse(localStorage.getItem('elementos'));
        }
        return elementoLS;
    }

    function eliminarProductosLocalStorage(elementoID) {
        let elementosLS = obtenerProductosLocalStorage();
        elementosLS = elementosLS.filter(elemento => elemento.id !== elementoID);
        localStorage.setItem('elementos', JSON.stringify(elementosLS));
    }

    function leerLocalStorage() {
        let elementosLS = obtenerProductosLocalStorage();
        elementosLS.forEach(function (elemento) {
            insertarCarrito(elemento);
        });
    }

    function comprarcarrito(e) {
        e.preventDefault();
        if (obtenerProductosLocalStorage().length === 0) {
            Swal.fire({
                icon: 'info',
                title: 'LO SENTIMOS',
                text: 'Tu carrito está vacío, agrega un producto',
                timer: 2000,
                showConfirmButton: false
            });
        } else {
            window.location.href = "/pago/";
        }
    }
});







