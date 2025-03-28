from datetime import datetime
from pytz import timezone

datetime_now = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
datetime_sp = datetime_now.astimezone(fuso_horario)
datetime_sp_string = datetime_sp.strftime('%d-%m-%Y %H:%M:%S')
