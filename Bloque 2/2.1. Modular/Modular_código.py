def obtener_subtotal_item(item):
    """Calcula el precio base de un item (precio * cantidad)."""
    return item['p'] * item['q']

def calcular_precio_con_descuento_estado(item):
    """Aplica descuentos basados en el estado ('s') del item."""
    subtotal = obtener_subtotal_item(item)
    
    # Mapeo de descuentos por estado para evitar if/else anidados
    descuentos = {1: 0.9, 2: 0.8}
    multiplicador = descuentos.get(item['s'], 1.0)
    
    return subtotal * multiplicador

def calcular_monto_por_tipo(item, tipo_cliente):
    """Aplica la lógica de negocio específica según el tipo de cliente."""
    if tipo_cliente == 'A':
        # Tipo A solo suma si el estado es 1
        return obtener_subtotal_item(item) if item['s'] == 1 else 0
    
    if tipo_cliente == 'B':
        # Tipo B tiene lógica de descuentos por estado
        return calcular_precio_con_descuento_estado(item)
    
    # Caso por defecto (el 'else' del código original)
    return obtener_subtotal_item(item)

def calcular_total_pedido(datos, tipo_cliente, descuento_total=0):
    """
    Función principal que orquesta el cálculo total.
    Sustituye a la función original p(d, t, dc).
    """
    total = sum(calcular_monto_por_tipo(item, tipo_cliente) for item in datos)
    
    if descuento_total > 0:
        total -= descuento_total
        
    return total