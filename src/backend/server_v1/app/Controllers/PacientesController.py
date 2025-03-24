from app.Models.Models import Paciente, db


class PacientesController:

    def __init__(self):
        pass


    def post_paciente(self, data):
        """
        Endpoint resposável por criar um novo paciente no banco de dados.
        """
        nome = data['nome']
        hc = data['HC']
        leito = data['leito']

        if (nome and hc and leito) and (isinstance(nome, str) and isinstance(hc, str) and isinstance(leito, str)):
            new = Paciente(nome=nome, HC=hc, Leito=leito)

            try:
                db.session.add(new)
                db.session.commit()
                return {
                    'id': new.id,
                    'nome': new.nome,
                    'HC': new.HC,
                    'leito': new.Leito
                }, 201


            except Exception as e:
                db.session.rollback()
                return {
                    'message': f'Erro ao criar paciente: {e}',
                    'code': 500
                }, 500


        return {
            'message': f"Dados inválidos",
            'code':400
        }, 400


    def get_pacientes(self):
        """
        Endpoint resposável por retornar todos os pacientes no banco de dados.
        """
        pacientes = Paciente.query.all()
        if pacientes:
            return pacientes
        

        return {
            'message':"Não existe nenhum paciente",
            'code':404
        }, 404


    def get_id_paciente(self, data):
        """
        Endpoint resposável por retornar um paciente no banco por id.
        """
        id = data['id']

        if id:

            paciente = Paciente.query.get(id)

            if paciente:
                return {
                    'id': paciente.id,
                    'nome': paciente.nome,
                    'HC': paciente.HC,
                    'leito': paciente.Leito
                }, 200
            

            return {
                'message': "Nenhum paciente com esse id...",
                'code': 404
            }, 404
        

        return {
            'message': "O id não é válido...",
            'code': 400
        }, 400 


    def get_nome_paciente(self, nome, leito): 
        """
        Endpoint resposável por retornar um paciente no banco por nome ou leito.
        """
        if (nome or leito) and (isinstance(nome, str) or isinstance(nome, str)) :
            paciente = Paciente.query.filter(
            (Paciente.nome == nome) | (Paciente.leito == leito)
            ).first()

            if paciente:

                return {
                    'id': paciente.id,
                    'nome': paciente.nome,
                    'HC': paciente.HC,
                    'leito': paciente.Leito
                }, 200
            
            return {
                'message': "Nenhum paciente encontrado...",
                'code': 404
            }, 404
        
        return {
            'message': "As informações não são válidas...",
            'code': 400
        }, 400     


    def put_paciente(self, data):
        id = data['id']
        new_nome = data['novo_nome']
        new_hc = data['novo_hc']
        new_leito = data['novo_leito']

        if id:

            paciente = Paciente.query.get(id)

            if paciente:
                paciente.nome = new_nome
                paciente.HC = new_hc
                paciente.Leito = new_leito

                try:
                    db.session.commit()
                    return {
                        'id': paciente.id,
                        'nome': paciente.nome,
                        'HC': paciente.HC,
                        'leito': paciente.Leito
                    }, 200 
                

                except Exception as e: 
                    return {
                        'message': f'Erro ao atualizar paciente: {e}',
                        'code': 500
                    }, 500       


            return {
                'message': "Nenhum paciente com esse id...",
                'code': 404
            }, 404
        

        return {
            'message': "O id não é válido...",
            'code': 400
        }, 400 


    
    def delete_paciente(self, data):
        id = data['id']

        if id:

            paciente = Paciente.query.get(id)

            if paciente:
                nome = paciente.nome
                HC = paciente.HC
                leito = paciente.Leito

                try:
                    db.session.delete(paciente)
                    db.session.commit()

                    return {
                        'message': f"O paciente, Nome:{nome}, HC:{HC}, Leito:{leito} foi removido do banco de dados com sucesso!",
                        'code': 200
                    }, 200
                except Exception as e:
                    return {
                        'message': f'Erro ao deletar paciente: {e}',
                        'code': 500
                    }, 500                     
            

            return {
                'message': "Nenhum paciente com esse id...",
                'code': 404
            }, 404
        

        return {
            'message': "O id não é válido...",
            'code': 400
        }, 400 