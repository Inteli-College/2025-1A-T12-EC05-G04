export default function Status() {
  return (
    <div className="status-content">
      <h2>Status: </h2>
      <div className="status-list">
        <div className="status-item">
          <div className="status-circle">
            <p>ON</p>
          </div>
          <p>Ligado</p>
        </div>

        <div className="status-item">
          <div className="status-circle">
            <p>OFF</p>
          </div>
            <p>Pronto para separar</p>
        </div>
        
        <div className="status-item">
          <div className="status-circle">
            <p className="error">!</p>
          </div>
          <p>Erro</p>
        </div>

    </div>

    </div>
  )
}