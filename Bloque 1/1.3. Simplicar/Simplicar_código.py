# Constantes semánticas para mejorar la intención del código
DESC_ESTADO_1_TIPO_B = 0.9
DESC_ESTADO_2_TIPO_B = 0.8
SIN_DESCUENTO = 1.0

def calcular_precio_total(datos, tipo, descuento_adicional=0):
    total = 0
    
    for item in datos:
        precio = item['p']
        cantidad = item['q']
        estado = item['s']
        subtotal_base = precio * cantidad

        # Cláusula de guarda para Tipo A
        if tipo == 'A':
            if estado == 1:
                total += subtotal_base
            continue # Early continue: salta a la siguiente iteración

        # Cláusula de guarda para Tipo B
        if tipo == 'B':
            if estado == 1:
                total += subtotal_base * DESC_ESTADO_1_TIPO_B
            elif estado == 2:
                total += subtotal_base * DESC_ESTADO_2_TIPO_B
            else:
                total += subtotal_base
            continue

    # Lógica final fuera del bucle
    if descuento_adicional > 0:
        total -= descuento_adicional
        
    return total