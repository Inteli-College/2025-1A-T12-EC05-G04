import SideBar from "./components/Sidebar";
import Status from "./components/Status";

export default function Separacao() {
  return (
    <div className="screen">
        <SideBar />
      <div className='content'>
        <Status />
      </div>
    </div>
  );
}