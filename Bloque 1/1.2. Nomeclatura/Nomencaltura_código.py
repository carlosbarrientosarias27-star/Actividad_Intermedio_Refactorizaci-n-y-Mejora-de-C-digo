from dataclasses import dataclass
from typing import List

@dataclass
class Producto:
    precio: float
    cantidad: int
    estado: int  # 1: Normal, 2: Liquidación, etc.

def calcular_total_pedido(productos: List[Producto], tipo_cliente: str, descuento_extra: float = 0) -> float:
    total = 0.0
    
    for item in productos:
        subtotal_item = item.precio * item.cantidad
        
        if tipo_cliente == 'A':
            if item.estado == 1:
                total += subtotal_item
        
        elif tipo_cliente == 'B':
            # Aplicar reglas de descuento por estado
            if item.estado == 1:
                total += subtotal_item * 0.9  # Descuento Socio
            elif item.estado == 2:
                total += subtotal_item * 0.8  # Descuento Liquidación
            else:
                total += subtotal_item
                
    if descuento_extra > 0:
        total -= descuento_extra
        
    return max(0, total) # Evitar totales negativos