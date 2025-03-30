import SideBar from "./components/Sidebar";
import MontagemItem from "./components/MontagemItem";
import styles from '../styles/Pendentes.module.css';

export default function Emergencia() {
  return (
    <div className="screen">
      <SideBar />
      <div className="content">
        <div className="emergencia-content">
          <div>
            <input type="text" id="nome-paciente" placeholder="Nome do paciente"></input>
            <div className="leito-hc">
              <input type="text" id="leito" placeholder="Leito"></input>
              <input type="text" id="hc" placeholder="HC"></input>
            </div>
            <input type="text" id="enfermeiro-responsavel" placeholder="Enfermeiro responsável"></input>
            <textarea type="text" id="medicamentos" placeholder="Medicamentos"></textarea>
            <textarea type="text" id="observacoes" placeholder="Observações"></textarea>
          </div>
          <div id="emergencia-right">
            <input type="date" id="data"></input>
            <button className="emergencia-confirmar" id="emergencia-confirmar">CONFIRMAR</button>
          </div>
        </div>
      </div>
    </div>
  );
}
