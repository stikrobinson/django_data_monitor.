from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required

import requests
from django.conf import settings

from datetime import date

def base(request):
    # return HttpResponse("¡Bienvenido a la aplicación Django!")
    return render(request, 'dashboard/base.html')

@login_required
@permission_required('dashboard.index_viewer', raise_exception=True)
def index(request):
    response = requests.get(settings.API_URL)  # URL de la API
    posts = response.json()  # Convertir la respuesta a JSON
    
    # [INDICADOR 1] - Número total de respuestas
    total_responses = len(posts)

    # [INDICADOR 2] - Conteo de asuntos (Asunto mas repetido)
    texto_subject = {
    'pack-4': "Pack 4 clases",
    'consulta': "Consulta",
    'clase-unica': "Clase única",
    'clase-presencial': "Clase presencial",
    'otros': "Otros",
    }
    conteo_subject = {
    'pack-4': 0,
    'consulta': 0,
    'clase-unica': 0,
    'clase-presencial': 0,
    'otros': 0,
    }

    # [INDICADOR 3/4] - fecha con mas respuestas / Fecha mas reciente
    conteo_fechas = {}
    fecha_mas_reciente = date(1, 1, 1)

    for post in posts.values():
        
        subject = post['subject']
        if subject in conteo_subject:
            conteo_subject[subject] += 1
        else:
            conteo_subject["otros"] += 1

        try:
            fecha = post['date']
        except KeyError:
            fecha = None

        if fecha:
            fechaActual = date(int(fecha.split('/')[2]), int(fecha.split('/')[1]), int(fecha.split('/')[0]))
            if fechaActual > fecha_mas_reciente:
                fecha_mas_reciente = fechaActual

            if fecha in conteo_fechas:
                conteo_fechas[fecha] += 1
            else:
                conteo_fechas[fecha] = 1
        
    valor_mas_repetido = max(conteo_subject, key=conteo_subject.get)

    fecha_mas_repetida = max(conteo_fechas, key=conteo_fechas.get)

    # [TABLA]
    datos_usuario = []
    for post in posts.values():
        datos_usuario.append({"nombre": post["name"], "correo": post["email"]})

    #datos cargados desde el servidor
    data = {
        'title': "Landing Page' Dashboard",
         'total_responses': total_responses,
         'subject_mas_repetida': texto_subject[valor_mas_repetido],
         'subject_valor': conteo_subject[valor_mas_repetido],
         'fecha_mas_respuestas': fecha_mas_repetida,
         'valor_fecha_mas_Respuestas': conteo_fechas[fecha_mas_repetida],
         'datos_usuario': datos_usuario,
         'conteo_subject': conteo_subject,
         'fecha_mas_reciente': fecha_mas_reciente,
    }
    return render(request, 'dashboard/index.html', data)