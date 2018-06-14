import random
def promedio_de_perdida(probabilidad):

    cantidad_envios_mensuales = 300
    p = 0
    p_anterior = 0
    cant_tiradas = 0.0
    max_cantidad_perdido= 0
    paquete_consecutivo = 0

    while cant_tiradas <= cantidad_envios_mensuales:
        tirada = nave_viajar(probabilidad)
        while tirada == perdido and  cant_tiradas <= cantidad_envios_mensuales:
            paquete_consecutivo = paquete_consecutivo + 1
            cant_tiradas = cant_tiradas + 1
            tirada = nave_viajar(probabilidad)
        if paquete_consecutivo > max_cantidad_perdido:
            max_cantidad_perdido = paquete_consecutivo
        paquete_consecutivo = 0;
        
    # devolvemos la probabilidad de huir
    return max_cantidad_perdido

perdido="perdido"
no_perdido="no_perdido"
def nave_viajar(probabilidad):
    return perdido if random.random()<probabilidad else no_perdido
