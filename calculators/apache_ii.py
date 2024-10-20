# app/calculators/apache_ii.py

def calculate_apache_ii(temperature, map_value, heart_rate, respiratory_rate, ph, sodium, potassium, creatinine, hematocrit, wbc, gcs, age, chronic_health):
    apache_score = 0

    # 1. Temperatura corporal (°C)
    if 36.0 <= temperature <= 38.4:
        apache_score += 0
    elif 38.5 <= temperature <= 38.9 or 34.0 <= temperature <= 35.9:
        apache_score += 1
    elif 32.0 <= temperature <= 33.9:
        apache_score += 2
    elif 30.0 <= temperature <= 31.9 or 39.0 <= temperature <= 40.9:
        apache_score += 3
    else:
        apache_score += 4

    # 2. Pressão Arterial Média (MAP) (mmHg)
    if 70 <= map_value <= 109:
        apache_score += 0
    elif map_value < 70 or map_value > 110:
        apache_score += 2

    # 3. Frequência cardíaca (bpm)
    if 70 <= heart_rate <= 109:
        apache_score += 0
    elif heart_rate < 70 or heart_rate > 109:
        apache_score += 1

    # 4. Frequência respiratória (respirações/min)
    if 12 <= respiratory_rate <= 24:
        apache_score += 0
    elif respiratory_rate < 12 or respiratory_rate > 24:
        apache_score += 1

    # 5. pH arterial
    if 7.33 <= ph <= 7.49:
        apache_score += 0
    elif ph < 7.33 or ph > 7.49:
        apache_score += 1

    # 6. Sódio plasmático (mmol/L)
    if 130 <= sodium <= 149:
        apache_score += 0
    elif sodium < 130 or sodium > 149:
        apache_score += 1

    # 7. Potássio plasmático (mmol/L)
    if 3.5 <= potassium <= 5.4:
        apache_score += 0
    elif potassium < 3.5 or potassium > 5.4:
        apache_score += 1

    # 8. Creatinina plasmática (mg/dL)
    if 0.6 <= creatinine <= 1.4:
        apache_score += 0
    elif creatinine < 0.6 or creatinine > 1.4:
        apache_score += 1

    # 9. Hematócrito (%)
    if 30 <= hematocrit <= 45:
        apache_score += 0
    elif hematocrit < 30 or hematocrit > 45:
        apache_score += 1

    # 10. Leucócitos (células/mm³)
    if 3000 <= wbc <= 12000:
        apache_score += 0
    elif wbc < 3000 or wbc > 12000:
        apache_score += 1

    # 11. Escala de Coma de Glasgow (GCS)
    apache_score += (15 - gcs)  # O APACHE II usa 15 - GCS como pontuação

    # 12. Idade (anos)
    if 45 <= age <= 64:
        apache_score += 2
    elif 65 <= age <= 74:
        apache_score += 3
    elif age >= 75:
        apache_score += 5

    # 13. Condições crônicas
    if chronic_health:
        apache_score += 2  # Ajusta caso tenha comorbidades crônicas

    return apache_score
