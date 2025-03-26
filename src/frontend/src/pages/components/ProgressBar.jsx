import React from "react";
import styles from "../../styles/ProgressBar.module.css";

const ProgressBar = ({ name, progress }) => {
  return (
    <div className={styles.progressContainer}>
      <span className={styles.progressLabel}>{name}</span>
      <div className={styles.progressBar}>
        <div
          className={styles.progressFill}
          style={{ width: `${progress}%` }}
        />
      </div>
      <span className={styles.progressPercentage}>{progress}%</span>
    </div>
  );
};

export default ProgressBar;

