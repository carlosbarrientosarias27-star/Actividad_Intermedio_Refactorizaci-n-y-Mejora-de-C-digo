from abc import ABC, abstractmethod

# 1. Definimos la Interfaz de la Estrategia (Abierto para extensión)
class PricingStrategy(ABC):
    @abstractmethod
    def calculate_total(self, items):
        pass

# 2. Estrategia para Cliente Tipo A
class StrategyA(PricingStrategy):
    def calculate_total(self, items):
        total = 0
        for i in items:
            if i.get('s') == 1:
                total += i['p'] * i['q']
        return total

# 3. Estrategia para Cliente Tipo B
class StrategyB(PricingStrategy):
    def calculate_total(self, items):
        total = 0
        for i in items:
            p_q = i['p'] * i['q']
            s = i.get('s')
            if s == 1:
                total += p_q * 0.9
            elif s == 2:
                total += p_q * 0.8
            else:
                total += p_q
        return total

# 4. Estrategia para Otros Clientes (Default)
class StrategyDefault(PricingStrategy):
    def calculate_total(self, items):
        return sum(i['p'] * i['q'] for i in items)

# 5. Función Principal (Cerrada para modificación)
# Fíjate que ya no hay IFs para determinar el tipo de cliente
def p(d, strategy: PricingStrategy, dc=0):
    r = strategy.calculate_total(d)
    
    if dc > 0:
        r = r - (r * dc / 100)
        
    return r

# --- Ejemplo de ejecución ---
if __name__ == "__main__":
    datos_carrito = [
        {'p': 100, 'q': 2, 's': 1}, 
        {'p': 50, 'q': 1, 's': 2}
    ]

    # Para usarlo, simplemente pasamos la instancia de la estrategia deseada
    # Cliente Tipo B con 10% de descuento adicional
    resultado = p(datos_carrito, StrategyB(), dc=10)
    
    print(f"Total calculado: {resultado}")