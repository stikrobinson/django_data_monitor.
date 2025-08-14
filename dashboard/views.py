from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

import requests
from django.conf import settings

def base(request):
    # return HttpResponse("¡Bienvenido a la aplicación Django!")
    return render(request, 'dashboard/base.html')

@login_required
def index(request):
    response = requests.get(settings.API_URL)  # URL de la API
    posts = response.json()  # Convertir la respuesta a JSON
    
    # [INDICADOR 1] - Número total de respuestas
    total_responses = len(posts)

    # [INDICADOR 2] - Conteo de asuntos (Asunto mas repetido)
    conteo_subject = {
    'pack-4': 0,
    'consulta': 0,
    'clase-unica': 0,
    'otros': 0
    }

    # [INDICADOR 3] - fecha con mas respuestas
    conteo_fechas = {}

    for post in posts.values():
        
        subject = post['subject']
        if subject in conteo_subject:
            conteo_subject[subject] += 1
        else:
            conteo_subject['otros'] += 1

        try:
            fecha = post['date']
        except KeyError:
            fecha = None

        if fecha:
            if fecha in conteo_fechas:
                conteo_fechas[fecha] += 1
            else:
                conteo_fechas[fecha] = 1
        
    valor_mas_repetido = max(conteo_subject, key=conteo_subject.get)

    fecha_mas_repetida = max(conteo_fechas, key=conteo_fechas.get)

    



    # [INDICADOR 4] - 

    #datos cargados desde el servidor
    data = {
        'title': "Landing Page' Dashboard",
         'total_responses': total_responses,
         'subject_mas_repetida': valor_mas_repetido,
         'subject_valor': conteo_subject[valor_mas_repetido],
         'fecha_mas_respuestas': fecha_mas_repetida,
         'valor_fecha_mas_Respuestas': conteo_fechas[fecha_mas_repetida],
         
    }
    return render(request, 'dashboard/index.html', data)