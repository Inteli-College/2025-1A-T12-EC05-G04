import React, { useState } from 'react';
import SideBar from './components/Sidebar';
import styles from '../styles/HomePage.module.css';

const HomePage = () => {
  const [systemStatus, setSystemStatus] = useState({
    robotStatus: false,
    assemblyStatus: false
  });

  const toggleStatus = (statusType) => {
    setSystemStatus(prev => {
      // If trying to activate assembly, robot must be active first
      if (statusType === 'assemblyStatus' && !prev.robotStatus) {
        return prev;
      }

      // Toggle the specific status
      const newStatus = { ...prev };
      newStatus[statusType] = !prev[statusType];

      // If robot is turned off, also turn off assembly
      if (statusType === 'robotStatus' && !newStatus.robotStatus) {
        newStatus.assemblyStatus = false;
      }

      return newStatus;
    });
  };

  const StatusButton = ({ status, label, type }) => {
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

    // Variante 1: Off/Off
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

    // Variante 2: On/Off
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

    // Variante 3: On/On
    if (robotStatus && assemblyStatus) {
      return (
        <div className={`${styles.mainContent} ${styles.mainContentSystemActive}`}>
          <h2 className={styles.mainContentTitle}>Sistema Totalmente Operacional</h2>
          <div className={styles.mainContentDetails}>
            <p>Sistema de montagem está em funcionamento</p>
          </div>
        </div>
      );
    }

    return null;
  };

  return (
    <div className={styles.appScreen}>
      <SideBar />
      <div className={styles.appContent}>
        <div className={styles.systemStatusBar}>
          <div className={styles.statusButtonContainer}>
            <StatusButton 
              type="robotStatus" 
              label="Robô" 
            />
            <StatusButton 
              type="assemblyStatus" 
              label="Montagem" 
            />
          </div>
        </div>
        <MainContent />
      </div>
    </div>
  );
};

export default HomePage;