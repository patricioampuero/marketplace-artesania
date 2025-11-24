import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [productos, setProductos] = useState([])
  const [cargando, setCargando] = useState(true)

  // Esta función se ejecuta automáticamente al abrir la página
  useEffect(() => {
    // Le pedimos los datos a TU backend en Python
    axios.get('http://127.0.0.1:8000/productos/')
      .then((response) => {
        console.log("¡Datos recibidos!", response.data)
        setProductos(response.data)
        setCargando(false)
      })
      .catch((error) => {
        console.error("Error conectando con el backend:", error)
        setCargando(false)
      })
  }, [])

  return (
    <div className="container">
      <header style={{ textAlign: 'center', padding: '2rem 0' }}>
        <h1 style={{ color: '#d35400', fontSize: '2.5rem' }}>🇨🇱 Artesanía Chilena</h1>
        <p style={{ color: '#666' }}>Del artesano directo a tu hogar</p>
      </header>

      {cargando ? (
        <p style={{ textAlign: 'center' }}>Cargando productos...</p>
      ) : (
        <div style={{ 
          display: 'grid', 
          gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))', 
          gap: '20px',
          padding: '20px'
        }}>
          {productos.map((producto) => (
            <div key={producto.id} style={{ 
              border: '1px solid #ddd', 
              borderRadius: '10px', 
              padding: '15px', 
              backgroundColor: 'white',
              boxShadow: '0 4px 6px rgba(0,0,0,0.1)'
            }}>
              {/* Si hay imagen la mostramos, si no, ponemos una caja gris */}
              <div style={{ 
                height: '200px', 
                backgroundColor: '#eee', 
                borderRadius: '5px', 
                marginBottom: '10px',
                overflow: 'hidden'
              }}>
                {producto.image_url ? (
                  <img src={producto.image_url} alt={producto.title} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
                ) : (
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', height: '100%', color: '#999' }}>Sin Imagen</div>
                )}
              </div>
              
              <h3 style={{ margin: '10px 0', fontSize: '1.2rem' }}>{producto.title}</h3>
              <span style={{ 
                backgroundColor: '#e67e22', 
                color: 'white', 
                padding: '3px 8px', 
                borderRadius: '15px', 
                fontSize: '0.8rem' 
              }}>
                {producto.category}
              </span>
              
              <p style={{ color: '#555', fontSize: '0.9rem', height: '40px', overflow: 'hidden' }}>
                {producto.description}
              </p>
              
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '15px' }}>
                <span style={{ fontSize: '1.4rem', fontWeight: 'bold', color: '#333' }}>
                  ${producto.price.toLocaleString('es-CL')}
                </span>
                <button style={{ 
                  backgroundColor: '#27ae60', 
                  color: 'white', 
                  border: 'none', 
                  padding: '8px 15px', 
                  borderRadius: '5px', 
                  cursor: 'pointer',
                  fontWeight: 'bold'
                }}>
                  Comprar
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
      
      {productos.length === 0 && !cargando && (
        <p style={{ textAlign: 'center', color: '#999' }}>No hay productos. ¡Ve a la API docs y crea uno!</p>
      )}
    </div>
  )
}

export default App