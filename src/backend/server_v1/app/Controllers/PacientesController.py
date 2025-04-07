from app.Models.PacienteModel import Paciente, db


class PacientesController:

    def __init__(self):
        pass


    def postPaciente(self, data):
        """
        Endpoint resposável por criar um novo paciente no banco de dados.
        """
        nome = data['nome']
        hc = data['hc']
        leito = data['leito']

        if (nome and hc and leito) and (isinstance(nome, str) and isinstance(hc, str) and isinstance(leito, str)):
            new = Paciente(nome=nome, HC=hc, Leito=leito)

            try:
                db.session.add(new)
                db.session.commit()
                return {
                    'id': new.id,
                    'nome': new.nome,
                    'hc': new.HC,
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


    def getPacientes(self):
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


    def getIdPaciente(self, data):
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
                    'hc': paciente.HC,
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


    def getNomePaciente(self, data): 
        """
        Endpoint resposável por retornar um paciente no banco por nome ou leito.
        """
        nome = data['nome']

        if (nome) and isinstance(nome, str) :
            paciente = Paciente.query.filter(Paciente.nome == nome).first()

            if paciente:

                return {
                    'id': paciente.id,
                    'nome': paciente.nome,
                    'hc': paciente.HC,
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

    def getLeitoPaciente(self, data):
        leito = data['leito']

        if (leito) and isinstance(leito, str) :
            paciente = Paciente.query.filter(Paciente.Leito == leito).first()

            if paciente:

                return {
                    'id': paciente.id,
                    'nome': paciente.nome,
                    'hc': paciente.HC,
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


    def putPaciente(self, data):
        id = data['id']
        new_nome = ["nome", data['nome']]
        new_hc = ["HC", data['hc']]
        new_leito = ["Leito", data['leito']]
        verdade = [new_nome, new_hc, new_leito]

        if id:
            paciente = Paciente.query.get(id)

            if paciente:
                for i in verdade:

                    if not isinstance(i[1], str) or not i[1] or i[1] == '':
                        i[1] = "Inválido"                      
                
                for i in range(len(verdade)):
                    value = verdade[i]
                    if value[1] != "Inválido":
                        setattr(paciente, value[0], value[1])
                    
                try:
                    db.session.commit()
                    return {
                        'id': paciente.id,
                        'nome': paciente.nome,
                        'hc': paciente.HC,
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

    
    def deletePaciente(self, data):
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
    
    def getHCPaciente(self, hc_paciente):
        try:
            paciente = Paciente.query.filter_by(HC=hc_paciente).first()
            if paciente:
                return paciente, 200
            else:
                return {"erro": "Paciente não encontrado"}, 404
        except Exception as e:
            return {"erro": str(e)}, 404
   