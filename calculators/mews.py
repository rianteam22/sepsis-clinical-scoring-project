# app/calculators/mews.py

def calculate_mews(respiratory_rate, heart_rate, systolic_bp, temperature, avpu):
    mews_score = 0

    # 1. Frequência respiratória (respirações por minuto)
    if respiratory_rate <= 8 or respiratory_rate >= 25:
        mews_score += 3
    elif 21 <= respiratory_rate <= 24:
        mews_score += 2
    elif 15 <= respiratory_rate <= 20:
        mews_score += 1
    else:
        mews_score += 0

    # 2. Frequência cardíaca (batimentos por minuto)
    if heart_rate <= 40 or heart_rate >= 130:
        mews_score += 3
    elif 111 <= heart_rate <= 129:
        mews_score += 2
    elif 101 <= heart_rate <= 110 or 41 <= heart_rate <= 50:
        mews_score += 1
    else:
        mews_score += 0

    # 3. Pressão arterial sistólica (mmHg)
    if systolic_bp <= 70:
        mews_score += 3
    elif 71 <= systolic_bp <= 80:
        mews_score += 2
    elif 81 <= systolic_bp <= 100:
        mews_score += 1
    else:
        mews_score += 0

    # 4. Temperatura corporal (°C)
    if temperature < 35 or temperature > 38.5:
        mews_score += 2
    elif 35 <= temperature <= 38.4:
        mews_score += 0

    # 5. Nível de consciência (AVPU)
    if avpu == "A":  # Alert
        mews_score += 0
    elif avpu == "V":  # Responding to Voice
        mews_score += 1
    elif avpu == "P":  # Responding to Pain
        mews_score += 2
    elif avpu == "U":  # Unresponsive
        mews_score += 3

    return mews_score
