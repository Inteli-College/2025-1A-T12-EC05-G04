import axios from "axios";

export default function MontagemButton({ idMontagem }) {
  const iniciarMontagem = async () => {
    console.log("Clique detectado!");
    console.log("ID da montagem:", idMontagem);

    try {
      const res = await axios.post("http://localhost:5000/robo/", {
        id: idMontagem,
      });
      console.log("Resposta do robô:", res.data);
    } catch (error) {
      console.error("Erro ao iniciar montagem:", error);
    }
  };

  return (
    <button className="montagem-button" onClick={iniciarMontagem}>
      <p>INICIAR MONTAGEM</p>
    </button>
  );
}