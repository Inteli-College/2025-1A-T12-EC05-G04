import MontagemButton from "./MontagemButton";


export default function MontagemItem() {
  return (
  <div className="montagem-item">
    <div className=" montagem-texts">
      <p>Nome do Paciente: </p>
      <div>
        <p>HC: </p>
        <p>LEITO: </p>
      </div>
    </div>
    <MontagemButton />
  </div>
  );
}