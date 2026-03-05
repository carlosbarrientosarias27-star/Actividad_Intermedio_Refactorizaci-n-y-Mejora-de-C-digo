# 1. Dependencia (Mock) para evitar advertencias del linter
def save_to_db(item: dict, message: str):
    """Simula el guardado en base de datos."""
    print(f"[DATABASE] {item['name']} (ID: {item['id']}): {message}")

# 2. Mapeo de Datos (Strategy Pattern simplificado)
# Para añadir 50 descuentos, solo agregas elementos a este diccionario.
DISCOUNT_RATES = {
    "SUMMER": 0.8,
    "WINTER": 0.7,
    "FLASH": 0.5,
    "BLACK_FRIDAY": 0.6,
    "WELCOME": 0.9
}

def apply_seasonal_discounts(items: list, discount_type: str):
    """
    Procesa descuentos masivos de forma escalable.
    """
    # PASO 1: Guard Clauses (Validaciones de salida temprana)
    if items is None or len(items) == 0:
        print("Error: No items to process")
        return

    discount_rate = DISCOUNT_RATES.get(discount_type)
    if not discount_rate:
        print(f"Warning: Discount type '{discount_type}' not supported")
        return

    # PASO 2: Lógica Principal (Sin anidamiento excesivo)
    for item in items:
        item['price'] *= discount_rate
        
        # Log unificado (Elimina la duplicación de código)
        print(f"Updating item: {item['id']}")
        save_to_db(item, f"Applied {discount_type} Discount")

# --- Prueba de ejecución ---
inventario = [{"id": 1, "name": "Camiseta", "price": 20.0}]
apply_seasonal_discounts(inventario, "SUMMER")