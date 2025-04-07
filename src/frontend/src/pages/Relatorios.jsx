import SideBar from './components/Sidebar';
import styles from '../styles/Relatorios.module.css';
import SearchBarRelatorios from './components/SearchBarRelatorios';
import MetricasRobo from './components/MetricasRobo';
import Graficos from './components/Graficos';

export default function Relatorios() {
    
    return (
        <div className='screen'>
                <SideBar />
                <div className="content">
                    <h1 className={styles.title}>Relatórios</h1>
                    <SearchBarRelatorios />
                    <MetricasRobo />
                    <Graficos />
                </div>
        </div>
    )
}