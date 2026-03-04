def calcular_total_pedido(lista_productos, tipo_cliente, descuento_adicional=0):
    total_acumulado = 0
    
    for producto in lista_productos:
        precio = producto['p']
        cantidad = producto['q']
        estado_stock = producto['s']
        subtotal = precio * cantidad
        
        if tipo_cliente == 'A':
            if estado_stock == 1:
                total_acumulado += subtotal
        elif tipo_cliente == 'B':
            if estado_stock == 1:
                total_acumulado += subtotal * 0.9
        elif estado_stock == 2:
            total_acumulado += subtotal * 0.8
        else:
            total_acumulado += subtotal
            
    if descuento_adicional > 0:
        total_acumulado -= (total_acumulado * descuento_adicional / 100)
        
    return total_acumulado