import SideBar from "./components/Sidebar";
import MontagemItem from "./components/MontagemItem";
import styles from '../styles/Pendentes.module.css';

export default function Pendentes() {
  return (
    <div className="screen">
      <SideBar />
      <div className="content">
        <h1 className="montagem-title">Montagens Pendentes</h1>
        <div className={styles.montagemContainer}>
          <MontagemItem />
          <MontagemItem />
          <MontagemItem />
          <MontagemItem />
          <MontagemItem />
          <MontagemItem />
        </div>
      </div>
    </div>
  );
}
