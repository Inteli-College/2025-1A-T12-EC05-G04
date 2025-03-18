import { useNavigate } from 'react-router-dom';
import styles from '../styles/Login.module.css';

export default function Login() {

    const navigate = useNavigate();

    const goToHome = () => {
        navigate('/home');
    };

    return (

        <div className={styles.containerGeral}>
            <div className={styles.containerImagem}>
            </div>

            <div className={styles.containerForms}>
                <div className={styles.containerCampos}>

                    <h2 className={styles.bemVindo}>Bem vindo(a) de volta!</h2>

                    <form className={styles.form}>
                        <p className={styles.placeholder}>E-mail</p>
                        <input type='email' placeholder='E-mail' className={styles.input} />
                        <p className={styles.placeholder}>Senha</p>
                        <input type='password' placeholder='Senha' className={styles.input} />
                    </form>

                    <a href="#" className={styles.esqueceuSenha}>Esqueceu sua senha?</a>

                    <button type='button' className={styles.button} onClick={goToHome}>Login</button>
                </div>
            </div>
        </div>
    );
}