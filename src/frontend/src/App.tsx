// src/App.jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Login from './pages/Login';
import Pendentes from './pages/Pendentes';
import Estoque from './pages/Estoque';
import Relatorios from './pages/Relatorios'
import Emergencia from './pages/Emergencia'

function App() {
  return (
    <BrowserRouter>
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/home" element={<Home />} />
          <Route path="/pendentes" element={<Pendentes />} />
          <Route path="/estoque" element={<Estoque />} />
          <Route path="/relatorios" element={<Relatorios />} />
          <Route path="/emergencia" element={<Emergencia />} />
        </Routes>
    </BrowserRouter>
  );
}

export default App;