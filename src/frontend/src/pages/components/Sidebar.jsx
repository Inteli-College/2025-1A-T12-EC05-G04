import { useNavigate } from 'react-router-dom';

export default function SideBar() {

  const navigate = useNavigate();

  const goToHome = () => {
      navigate('/home');
  };

  const goToPendentes = () => {
      navigate('/pendentes');
  };

  const goToSeparacoes = () => {
      navigate('/separacao');
  };

  const goToEmergencia = () => {
    navigate('/emergencia');
};

  return (
    <div className="sidebar-content">
      <img id="logo" src="../../assets/react.svg"></img>
      <div className="sb-button-section">
        <div>
          <button className="button-home" onClick={goToHome}></button>
          <p>Home</p>
        </div>
        <div>
          <button className="" onClick={goToPendentes}></button>
          <p>Pendentes</p>
        </div>
        <div>
          <button className="" onClick={goToSeparacoes}></button>
          <p>Separação</p>
        </div>
        <div>
          <button className=""></button>
          <p>Lorem</p>
        </div>
        <div>
          <button className="" onClick={goToEmergencia}></button>
          <p>Emergências</p>
        </div>
      </div>
    </div>
  );
}