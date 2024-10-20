# app/calculators/sos.py

def calculate_sos(temperature, systolic_bp, heart_rate, respiratory_rate, spo2, wbc, lactate):
    sos_score = 0

    # 1. Temperatura corporal (°C)
    if temperature < 36 or temperature > 38:
        sos_score += 1

    # 2. Pressão arterial sistólica (mmHg)
    if systolic_bp <= 90:
        sos_score += 2

    # 3. Frequência cardíaca (batimentos por minuto)
    if heart_rate >= 100:
        sos_score += 1

    # 4. Frequência respiratória (respirações por minuto)
    if respiratory_rate >= 21:
        sos_score += 1

    # 5. Saturação de oxigênio (SpO₂)
    if spo2 < 93:
        sos_score += 1

    # 6. Contagem de leucócitos (WBC)
    if wbc < 4000 or wbc > 12000:
        sos_score += 1

    # 7. Ácido láctico (Lactato)
    if lactate >= 2:
        sos_score += 1

    return sos_score
