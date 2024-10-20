# app/calculators/saps_3.py

def calculate_saps_3(age, comorbidities, prior_stay, heart_rate, systolic_bp, pao2_fio2, mechanical_ventilation, temperature, wbc, platelets, ph, creatinine, bilirubin):
    saps_score = 0

    # 1. Idade
    if age < 40:
        saps_score += 0
    elif 40 <= age < 60:
        saps_score += 6
    elif 60 <= age < 70:
        saps_score += 8
    elif 70 <= age < 75:
        saps_score += 13
    elif 75 <= age < 80:
        saps_score += 15
    else:
        saps_score += 18

    # 2. Comorbidades
    if comorbidities:
        saps_score += 6  # Valor ajustável com base nas condições de comorbidade

    # 3. Dias de internação prévia
    if prior_stay >= 28:
        saps_score += 7
    elif 14 <= prior_stay < 28:
        saps_score += 6
    else:
        saps_score += 0

    # 4. Frequência cardíaca
    if heart_rate >= 120:
        saps_score += 4
    elif 70 <= heart_rate < 120:
        saps_score += 0

    # 5. Pressão arterial sistólica
    if systolic_bp < 70:
        saps_score += 11
    elif 70 <= systolic_bp < 120:
        saps_score += 8
    else:
        saps_score += 0

    # 6. PaO₂/FiO₂
    if pao2_fio2 < 100 and mechanical_ventilation:
        saps_score += 11
    elif pao2_fio2 < 60:
        saps_score += 5

    # 7. Temperatura
    if temperature < 34.5:
        saps_score += 7
    else:
        saps_score += 0

    # 8. Leucócitos
    if wbc < 3000 or wbc > 20000:
        saps_score += 2

    # 9. Plaquetas
    if platelets < 50000:
        saps_score += 8
    elif 50000 <= platelets < 100000:
        saps_score += 3

    # 10. pH arterial
    if ph <= 7.25:
        saps_score += 3

    # 11. Creatinina
    if creatinine >= 3.5:
        saps_score += 8
    elif creatinine >= 2.0:
        saps_score += 7

    # 12. Bilirrubina
    if bilirubin >= 6.0:
        saps_score += 8
    elif 2.0 <= bilirubin < 6.0:
        saps_score += 4

    return saps_score
