import { useNavigate } from 'react-router-dom';
import logo from '../../assets/logo.png'

export default function SideBar() {

  const navigate = useNavigate();

  const goToHome = () => {
      navigate('/home');
  };

  const goToPendentes = () => {
      navigate('/pendentes');
  };

  const goToEstoque = () => {
      navigate('/estoque');
  };

  const goToRelatorios = () => {
    navigate('/relatorios');
};

const goToEmergencia = () => {
  navigate('/emergencia');
};

  return (
    <div className="sidebar-content">
      <img id="logo" src={logo} alt=""></img>
      <div className="sb-button-section">
        <div>
          <button className="button-home" onClick={goToHome}></button>
          <p>Home</p>
        </div>
        <div>
          <button className="button-pendentes" onClick={goToPendentes}></button>
          <p>Pendentes</p>
        </div>
        <div>
          <button className="button-estoque" onClick={goToEstoque}></button>
          <p>Estoque</p>
        </div>
        <div>
          <button className="button-relatorios" onClick={goToRelatorios}></button>
          <p>Relatórios</p>
        </div>
        <div>
          <button className="button-emergencia" onClick={goToEmergencia}></button>
          <p>Emergência</p>
        </div>
      </div>
    </div>
  );
}