def calcular_subtotal_item(item):
    """Responsabilidad: Calcular el precio base (precio * cantidad) de un producto."""
    return item['p'] * item['q']

def obtener_precio_ajustado(item, tipo_cliente):
    """Responsabilidad: Aplicar reglas de negocio según el tipo de cliente y estado del producto."""
    subtotal = calcular_subtotal_item(item)
    estado = item['s']

    # Lógica para Cliente Tipo A
    if tipo_cliente == 'A':
        return subtotal if estado == 1 else 0
    
    # Lógica para Cliente Tipo B (aplica descuentos del 10% o 20% según estado)
    if tipo_cliente == 'B':
        if estado == 1:
            return subtotal * 0.9
        if estado == 2:
            return subtotal * 0.8
        return 0
            
    # Caso por defecto
    return subtotal

def aplicar_descuento_global(total_acumulado, porcentaje_descuento):
    """Responsabilidad: Aplicar el descuento final al monto total calculado."""
    if porcentaje_descuento > 0:
        return total_acumulado * (1 - porcentaje_descuento / 100)
    return total_acumulado

def procesar_total_pedido(lista_items, tipo_cliente, descuento_total=0):
    """
    Responsabilidad: Orquestar el cálculo sumando cada ítem y aplicando el descuento final.
    Sustituye a la función original p(d, t, dc).
    """
    total = sum(obtener_precio_ajustado(item, tipo_cliente) for item in lista_items)
    return aplicar_descuento_global(total, descuento_total)