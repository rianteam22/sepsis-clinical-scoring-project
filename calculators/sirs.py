# app/calculators/sirs.py

def calculate_sirs(temperature, heart_rate, respiratory_rate, wbc, paCO2=None, bands=None):
    sirs_score = 0

    # 1. Temperatura > 38°C ou < 36°C
    if temperature > 38 or temperature < 36:
        sirs_score += 1

    # 2. Frequência cardíaca > 90 bpm
    if heart_rate > 90:
        sirs_score += 1

    # 3. Frequência respiratória > 20 respirações por minuto ou PaCO2 < 32 mmHg
    if respiratory_rate > 20 or (paCO2 is not None and paCO2 < 32):
        sirs_score += 1

    # 4. Contagem de leucócitos > 12.000/mm³ ou < 4.000/mm³ ou bandas > 10%
    if wbc > 12000 or wbc < 4000 or (bands is not None and bands > 10):
        sirs_score += 1

    return sirs_score
