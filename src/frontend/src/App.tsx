// src/App.jsx
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import Login from './pages/Login';
import Pendentes from './pages/Pendentes';
import Separacao from './pages/Separacao';
import store from './redux/store';
import { Provider } from 'react-redux';


function App() {
  return (
    <Provider store={store}>
      <BrowserRouter>
          <Routes>
            <Route path="/" element={<Login />} />
            
              <Route path="/home" element={<Home />} />

            <Route path="/pendentes" element={<Pendentes />} />
            <Route path="/separacao" element={<Separacao />} />
          </Routes>
      </BrowserRouter>
    </Provider>
  );
}

export default App;