from datetime import datetime

def electricity_price(hour, weekday, cycle_type="Two-cycle", price_model="Fixed"):
    """
    Calculates the electricity price based on hour and tariff cycle.
    In Portugal, there are different tariffs depending on the cycle type (Simple, Two-cycle, or Three-cycle) and the price model (Fixed or Variable).
    """

    cycle_alias = {
        "Simples": "Simple",
        "Bi-horária": "Two-cycle",
        "Biciclo": "Two-cycle",
        "Tri-horária": "Three-cycle",
        "Triciclo": "Three-cycle",
    }
    price_alias = {
        "Preço fixo": "Fixed",
        "Fixo": "Fixed",
        "Preço variável": "Variable",
        "Variável": "Variable",
    }

    cycle_type = cycle_alias.get(cycle_type, cycle_type)
    price_model = price_alias.get(price_model, price_model)

    # ERSE regulated tariffs 2024/2025, BTN ≤ 20.7 kVA (€/kWh, inc. VAT)
    if cycle_type == "Simple":
        if price_model == "Fixed":
            return 0.2196
        else:
            return 0.14 if (hour < 7 or hour >= 23) else 0.22  # simulated indexed

    elif cycle_type == "Two-cycle":
        # Vazio: 22h–08h weekdays, all weekend
        is_off_peak = (hour >= 22 or hour < 8) or weekday >= 5
        if price_model == "Fixed":
            return 0.1246 if is_off_peak else 0.2626
        else:
            return 0.10 if is_off_peak else 0.22  # simulated indexed

    elif cycle_type == "Three-cycle":
        # Ponta: 09h–12h and 18h–21h weekdays
        is_peak = weekday < 5 and ((9 <= hour < 12) or (18 <= hour < 21))
        # Vazio: 00h–08h and 22h–24h weekdays, all weekend
        is_off_peak = (hour >= 22 or hour < 8) or weekday >= 5
        if price_model == "Fixed":
            if is_peak:
                return 0.2876
            elif is_off_peak:
                return 0.1046
            else:
                return 0.1966  # cheias
        else:
            if is_peak:
                return 0.26
            elif is_off_peak:
                return 0.09
            else:
                return 0.18  # simulated indexed