import SideBar from "./components/Sidebar";
import Status from "./components/Status";
import StatusPaciente from "./components/StatusPaciente";
import Bipagem from "./components/BipagemProcesso";

export default function Separacao() {
  return (
    <div className="screen">
        <SideBar />
      <div className='content separacao'>
        <Status />
        <StatusPaciente />
        <div className="bipagem">
        </div>
        <Bipagem />
        <div className="id-fita">
          <p>Fita #00001: em montagem</p>
        </div>
      </div>
    </div>
  );
}