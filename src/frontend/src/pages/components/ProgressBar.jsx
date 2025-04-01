import React from "react";
import styles from "../../styles/ProgressBar.module.css";

const ProgressBar = ({ name, progress }) => {
  return (
    <div className={styles.progressContainer}>
      <div className={styles.labelContainer}>
        <span className={styles.name}>{name}</span>
        <span className={styles.percentage}>{progress}%</span>
      </div>
      <div className={styles.barBackground}>
        <div
          className={styles.barFill}
          style={{ width: `${progress}%` }}
        ></div>
      </div>
    </div>
  );
};

export default ProgressBar;
