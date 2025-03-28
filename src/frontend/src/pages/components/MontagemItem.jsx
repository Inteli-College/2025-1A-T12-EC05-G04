import MontagemButton from "./MontagemButton";

export default function MontagemItem({ nomePaciente, hc, leito }) {
  return (
    <div className="montagem-item">
      <div className="montagem-texts">
        <p><strong>Nome do Paciente:</strong> {nomePaciente}</p>
        <div>
          <p>HC: {hc}</p>
          <p>LEITO: {leito}</p>
        </div>
      </div>
      <MontagemButton />
    </div>
  );
}