import random
def promedio_de_perdida(probabilidad,epsilon):
    envios = 0
    promedio = 0.0
    p_anterior = 0
    p = 0
    iteraciones = 2000
    while (abs(p - p_anterior) > epsilon or envios < 500) and envios <= iteraciones:
        envios = envios + 1
        promedio = promedio + envios_mensuales(probabilidad)
        p_anterior = p
        p = promedio / envios
    print(envios)
    return p_anterior

def envios_mensuales(probabilidad):
    cantidad_envios_mensuales = 300
    cant_tiradas = 0
    max_cantidad_perdido= 0
    paquete_consecutivo = 0
    while cant_tiradas < cantidad_envios_mensuales:
        tirada = nave_viajar(probabilidad)
        while tirada == perdido and  cant_tiradas < cantidad_envios_mensuales:
            paquete_consecutivo = paquete_consecutivo + 1
            cant_tiradas = cant_tiradas + 1
            tirada = nave_viajar(probabilidad)
        if paquete_consecutivo > max_cantidad_perdido:
            max_cantidad_perdido = paquete_consecutivo
        paquete_consecutivo = 0
        cant_tiradas = cant_tiradas + 1
    return max_cantidad_perdido

def probabilidad_despido(tipo,epsilon):
    


    return probabilidad

perdido="perdido"
no_perdido="no_perdido"
def nave_viajar(probabilidad):
    return perdido if random.random()<probabilidad else no_perdido
