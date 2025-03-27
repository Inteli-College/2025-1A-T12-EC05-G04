import SideBar from "./components/Sidebar";
import MontagemItem from "./components/MontagemItem";
import Status from "./components/Status";
import StatusPaciente from "./components/StatusPaciente";
import Bipagem from "./components/BipagemProcesso";
import styles from '../styles/Pendentes.module.css';

export default function Separacao() {
  return (
    <div className="screen">
      <SideBar />
      <div className='content separacao'>
        <Status />
        <hr className="line-status"></hr>
        <div className="status-paciente">
          <p className="paciente">Nome do Paciente</p>
          <div className="info">
            <p>Leito</p>
              <div></div>
            <p>Prontuário</p>
              <div></div>
            <p>HC</p>
              <div></div>
            <p>Fita</p>
          </div>
        </div>
        <div className="bipagem">
          <p>Bipagem</p>
          <p>Controle 1</p>
          <p>Controle 2</p>
        </div> 
        <Bipagem />
        <div className="id-fita">
          <p>Fita #00001: em montagem</p>
        </div>
      </div>
    </div>
  );
}