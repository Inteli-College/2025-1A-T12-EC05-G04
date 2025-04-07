export default function MetricasRobo () {
    return(
        <div className="metricas-container">
            <h1>Manipulador robótico</h1>
            <div className="metricas-cards-container">
                <div className="metricas-card">
                    <h2>Taxa de Ocupação</h2>
                    <p>75%</p>
                </div>
                <div className="metricas-card">
                    <h2>Tempo Médio de Espera</h2>
                    <p>5 minutos</p>
                </div>
                <div className="metricas-card">
                    <h2>Taxa de Erros</h2>
                    <p>1%</p>
                </div>
                <div className="metricas-card">
                    <h2>Tempo Médio de Resposta</h2>
                    <p>2 segundos</p>
                </div>
            </div>
        </div>
    )
}