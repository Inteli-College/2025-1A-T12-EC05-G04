import { useNavigate } from 'react-router-dom';
import styles from '../styles/Login.module.css';
import React, { useState, useEffect } from 'react';

export default function Login() {
    const navigate = useNavigate();
    const [email, setEmail] = useState('');
    const [senha, setSenha] = useState('');
    const [erro, setErro] = useState('');

    const handleLogin = async () => {
        try {
            const response = await fetch('http://localhost:5000/auth/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email, senha })
            });
    
            const data = await response.json();
    
            if (!response.ok) {
                setErro(data.erro || 'Erro ao fazer login');
                return;
            }
    
            console.log('Login bem-sucedido:', data);
    
            // Pega os dados do usuário pelo e-mail e salva no localStorage
            const sucesso = await handleNomeUser();
    
            if (!sucesso) {
                return; // se falhou ao buscar nome, para aqui
            }
    
            navigate('/home');
        } catch (error) {
            console.error('Erro ao logar:', error);
            setErro('Erro de conexão com o servidor');
        }
    };
    

    const handleNomeUser = async () => {
        try {
            const response = await fetch(`http://localhost:5000/auth/getUserName/${email}`);
            const data = await response.json();
    
            if (data.nome) {
                const usuario = {
                    nome: data.nome,
                    email: email,
                    id_usuario: data.id
                };
                localStorage.setItem("usuario", JSON.stringify(usuario));
                console.log("Usuário salvo:", usuario);
                return true; 
            } else {
                alert("Usuário não encontrado com esse e-mail.");
                return false;
            }
        } catch (error) {
            console.error("Erro ao buscar usuário:", error);
            alert("Erro ao buscar informações do usuário.");
            return false;
        }
    };
    


    return (
        <div className={styles.containerGeral}>
            <div className={styles.containerImagem}></div>

            <div className={styles.containerForms}>
                <div className={styles.containerCampos}>
                <h2 className={styles.bemVindo}>Bem vindo(a) de volta!</h2>
                <form className={styles.form} onSubmit={e => e.preventDefault()}>
                <p className={styles.placeholder}>E-mail</p>
                <input
                            type='email'
                            placeholder='E-mail'
                            className={styles.input}
                            value={email}
                            onChange={e => setEmail(e.target.value)}
                        />
                        <p className={styles.placeholder}>Senha</p>
                        <input
                            type='password'
                            placeholder='Senha'
                            className={styles.input}
                            value={senha}
                            onChange={e => setSenha(e.target.value)}
                        />
                    </form>

                    {erro && <p style={{ color: 'red' }}>{erro}</p>}
                    
                    <button type='button' className={styles.button} onClick={handleLogin}>
                        Login
                    </button>
                </div>
            </div>
        </div>
    );
}