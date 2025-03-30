export default function Emergencia() {
  return (
    <div className="screen">
      <SideBar />
      <div className="content">
        <div className="emergencia-content">
          <div>
            <input type="text" id="nome-paciente"></input>
            <input type="text" id="leito"></input>
            <input type="text" id="hc"></input>
            <input type="text" id="enfermeiro-responsavel"></input>
            <input type="text" id="medicamentos"></input>
            <input type="text" id="observacoes"></input>
          </div>
          <div>
            <input type="date" id="data"> </input>
            <button id="emergencia-confirmar">CONFIRMAR</button>
          </div>
        </div>
      </div>
    </div>
  );
}