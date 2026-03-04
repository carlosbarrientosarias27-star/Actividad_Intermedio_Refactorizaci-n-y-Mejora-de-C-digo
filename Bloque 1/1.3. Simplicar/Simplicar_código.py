# Constantes semánticas para evitar "números mágicos"
DISCOUNT_B_S1 = 0.9
DISCOUNT_S2 = 0.8
STATUS_ACTIVE = 1
STATUS_PENDING = 2

def p(d, t, dc=0):
    r = 0
    for i in d:
        price_base = i['p'] * i['q']
        
        # Guard Clauses & Early Returns (dentro del flujo del loop)
        if t == 'A':
            if i['s'] == STATUS_ACTIVE:
                r += price_base
            continue # Saltamos a la siguiente iteración

        if t == 'B':
            if i['s'] == STATUS_ACTIVE:
                r += price_base * DISCOUNT_B_S1
            continue

        if i['s'] == STATUS_PENDING:
            r += price_base * DISCOUNT_S2
            continue

        # Caso por defecto (el 'else' original)
        r += price_base

    # Aplicar descuento global al final
    if dc > 0:
        r -= (r * dc / 100)
        
    return r