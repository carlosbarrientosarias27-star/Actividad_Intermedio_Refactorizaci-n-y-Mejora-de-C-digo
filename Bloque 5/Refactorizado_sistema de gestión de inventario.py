# Mock de base de datos para evitar errores en VS Code
def save_to_db(item: dict, message: str):
    print(f"[DB] {item['name']} (ID: {item['id']}): {message}")

# Estrategia de descuentos (Elimina la duplicación)
DISCOUNT_MAP = {
    "SUMMER": 0.8,
    "WINTER": 0.7,
    "FLASH": 0.5
}

def apply_inventory_discounts(items: list, discount_type: str):
    """Aplica descuentos a una lista de productos y guarda en DB."""
    
    # Guard Clauses (Eliminan el anidamiento excesivo)
    if not items:
        print("Error: No items to process")
        return

    discount_rate = DISCOUNT_MAP.get(discount_type)
    if not discount_rate:
        print(f"Warning: Discount type '{discount_type}' not recognized")
        return

    for item in items:
        item['price'] *= discount_rate
        print(f"Updating item: {item['id']}")
        save_to_db(item, f"Applied {discount_type.capitalize()} Discount")

# Ejemplo de uso
inventory = [{"id": 101, "name": "Shirt", "price": 50.0}]
apply_inventory_discounts(inventory, "SUMMER")