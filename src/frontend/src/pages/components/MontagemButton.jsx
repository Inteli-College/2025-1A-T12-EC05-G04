import axios from "axios";

export default function MontagemButton({ idMontagem }) {
  const iniciarMontagem = () => {
    console.log("Clique detectado! ID da montagem:", idMontagem);

      
    // Dispara a requisição de forma assíncrona
    axios.post("http://localhost:5000/robo/", { id: idMontagem })
      .then(res => {
        console.log("Resposta do robô:", res.data);
      })
      .catch(error => {
        console.error("Erro ao iniciar montagem:", error);
      });

    // Redireciona imediatamente sem aguardar a resposta da requisição
    window.location.href = "/home";
  };

  return (
    <button className="montagem-button" onClick={iniciarMontagem}>
      <p>INICIAR MONTAGEM</p>
    </button>
  );
}
