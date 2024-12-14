import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';  // Archivo de estilos globales
import App from './app';  // Archivo de la aplicación

// Seleccionamos el contenedor donde se montará la aplicación
const root = ReactDOM.createRoot(document.getElementById('root'));

// Renderizamos el componente App en el contenedor root
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
