import React, { useState, useEffect } from 'react';
import SideBar from './components/Sidebar';
import ListaAtual from './components/Lista';
import ProgressBar from './components/ProgressBar';
import styles from '../styles/HomePage.module.css';

const HomePage = () => {
  const [systemStatus, setSystemStatus] = useState({
    robotStatus: false,
    assemblyStatus: false
  });

  const [medicines, setMedicines] = useState([]);

  const toggleStatus = (statusType) => {
    setSystemStatus(prev => {
      if (statusType === 'assemblyStatus' && !prev.robotStatus) {
        return prev;
      }

      const newStatus = { ...prev };
      newStatus[statusType] = !prev[statusType];

      if (statusType === 'robotStatus' && !newStatus.robotStatus) {
        newStatus.assemblyStatus = false;
        setMedicines([]);
      }

      return newStatus;
    });
  };

  useEffect(() => {
    if (systemStatus.robotStatus && systemStatus.assemblyStatus) {
      const interval = setInterval(() => {
        setMedicines(prev => prev.map(med => ({
          ...med,
          progress: med.progress < 100 ? med.progress + 10 : 100
        })));
      }, 1000);
  
      return () => clearInterval(interval);
    }
  }, [systemStatus, medicines]);
  

  const addMedicine = () => {
    if (systemStatus.robotStatus && systemStatus.assemblyStatus) {
      setMedicines(prev => [...prev, { name: `Remédio ${prev.length + 1}`, progress: 0 }]);
    }
  };

  const StatusButton = ({ label, type }) => {
    const isActive = systemStatus[type];
    
    return (
      <button 
        className={`${styles.statusButton} ${isActive ? styles.statusButtonActive : styles.statusButtonInactive}`}
        onClick={() => toggleStatus(type)}
        disabled={type === 'assemblyStatus' && !systemStatus.robotStatus}
      >
        {label}: {isActive ? 'Ativo' : 'Inativo'}
      </button>
    );
  };

  const MainContent = () => {
    const { robotStatus, assemblyStatus } = systemStatus;

    if (!robotStatus && !assemblyStatus) {
      return (
        <div className={`${styles.mainContent} ${styles.mainContentInactive}`}>
          <h2 className={styles.mainContentTitle}>Sistema Inativo</h2>
          <p className={styles.mainContentDescription}>
            Ative o robô para iniciar
          </p>
        </div>
      );
    }

    if (robotStatus && !assemblyStatus) {
      return (
        <div className={`${styles.mainContent} ${styles.mainContentRobotActive}`}>
          <h2 className={styles.mainContentTitle}>Robô Ativo</h2>
          <p className={styles.mainContentDescription}>
            Robô está pronto. Você pode ativar a montagem.
          </p>
        </div>
      );
    }

    if (robotStatus && assemblyStatus) {
      return (
        <div className={`${styles.mainContent} ${styles.mainContentSystemActive}`}>
          <ListaAtual />
          <button onClick={addMedicine} className={styles.addMedicineButton}>
          Adicionar Remédio
          </button>
          {medicines.map((med, index) => (
            <ProgressBar key={index} name={med.name} progress={med.progress} />
          ))}
        </div>
      );
    }
    

    return null;
  };

  return (
    <div className='screen'>
      <SideBar />
      <div className='content'>
      <div className={styles.topBar}>
        <div className={styles.statusButtonContainer}>
          <StatusButton type="robotStatus" label="Robô" />
          <StatusButton type="assemblyStatus" label="Montagem" />
        </div>
      </div>
        <MainContent />
      </div>
    </div>
  );
};

export default HomePage;
