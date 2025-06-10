from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
import locale
from .data import ORATIONS, MYSTERIES

class TercoAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
        except locale.Error:
            try:
                locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')
            except locale.Error:
                pass

        dia_semana_completo = datetime.now().strftime('%A').lower()

        dia_semana_hoje = dia_semana_completo.replace('-feira', '')

        if 'segunda' in dia_semana_hoje:
            dia_semana_hoje = 'segunda'
        elif 'terca' in dia_semana_hoje:
            dia_semana_hoje = 'terça' 
        elif 'quarta' in dia_semana_hoje:
            dia_semana_hoje = 'quarta'
        elif 'quinta' in dia_semana_hoje:
            dia_semana_hoje = 'quinta'
        elif 'sexta' in dia_semana_hoje:
            dia_semana_hoje = 'sexta'
        elif 'sabado' in dia_semana_hoje:
            dia_semana_hoje = 'sábado'
        elif 'domingo' in dia_semana_hoje:
            dia_semana_hoje = 'domingo'

        misterios_do_dia = {}
        for i, misterio_info in MYSTERIES.items():
            if dia_semana_hoje in misterio_info['dias']:
                misterios_do_dia = {
                    "titulo": misterio_info['titulo'],
                    "misterios": misterio_info['misterios']
                }
                break

        response_data = {
            "data_atual": datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            "dia_da_semana": dia_semana_hoje,
            "misterios_do_dia": misterios_do_dia,
            "oracoes": ORATIONS
        }
        return Response(response_data)