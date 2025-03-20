import SideBar from "./components/Sidebar";
import MontagemItem from "./components/MontagemItem";

export default function Pendentes() {
  return (
    <div className="screen">
        <SideBar />
      <div className='content'>
        <h1 className='montagem-title'>Montagens Pendentes</h1>
        <MontagemItem />
      </div>
    </div>
  );
}