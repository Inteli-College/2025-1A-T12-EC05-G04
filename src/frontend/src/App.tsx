// src/App.jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Login from './pages/Login';
import Pendentes from './pages/Pendentes';
import Separacao from './pages/Separacao';


function App() {
  return (
      <BrowserRouter>
          <Routes>
            <Route path="/" element={<Login />} />
            
              <Route path="/home" element={<Home />} />

            <Route path="/pendentes" element={<Pendentes />} />
            <Route path="/separacao" element={<Separacao />} />
          </Routes>
      </BrowserRouter>
  );
}

export default App;