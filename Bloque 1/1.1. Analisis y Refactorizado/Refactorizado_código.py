# Constantes para evitar Magic Numbers
DISCOUNT_TYPE_B = 0.9
DISCOUNT_STATUS_2 = 0.8

def calculate_order_total(items, customer_type, flat_discount_pct=0):
    """
    Calcula el precio total de una lista de productos aplicando 
    reglas de negocio por tipo de cliente y estado del item.
    """
    total = 0.0
    
    for item in items:
        price = item['price']
        quantity = item['quantity']
        status = item['status']
        
        subtotal = price * quantity
        
        # Aplicación de reglas de descuento
        if customer_type == 'A' and status == 1:
            total += subtotal
        elif customer_type == 'B' and status == 1:
            total += subtotal * DISCOUNT_TYPE_B
        elif status == 2:
            total += subtotal * DISCOUNT_STATUS_2
        else:
            total += subtotal

    # Aplicar descuento global si existe
    if flat_discount_pct > 0:
        total -= (total * flat_discount_pct / 100)
        
    return total