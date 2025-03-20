import React from 'react';
import styles from '../styles/Home.module.css';
import Layout from './components/Layout';

export default function Home() {
  return (
    <Layout>
      <div className={styles.body}>
        <div className={styles.containerGeral}>
          <div className={styles.containerStatus}>
            <div className={styles.statusItem}>
            <h2>Status:</h2>
            </div>
            <div className={styles.statusItem}>
              <div className={styles.onOff}>Off</div>
              <p className={styles.statusTag}>Desligado</p>
            </div>
            <div className={styles.statusItem}>
              <div className={styles.onOff}>Off</div>
              <p className={styles.statusTag}>Desligado</p>
            </div>
          </div>
          <div className={styles.quebra}></div>
          <div className={styles.containerInfos}></div>
        </div>
      </div>
    </Layout>
  );
}