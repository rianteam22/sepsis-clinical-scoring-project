# app/calculators/sofa.py

def calculate_sofa(pao2_fio2, platelets, bilirubin, map_value, vasopressor_use, gcs, creatinine):
    sofa_score = 0

    # 1. Respiração (PaO2/FiO2 ratio)
    if pao2_fio2 >= 400:
        sofa_score += 0
    elif 300 <= pao2_fio2 < 400:
        sofa_score += 1
    elif 200 <= pao2_fio2 < 300:
        sofa_score += 2
    elif 100 <= pao2_fio2 < 200:
        sofa_score += 3
    else:
        sofa_score += 4

    # 2. Coagulação (Plaquetas)
    if platelets >= 150:
        sofa_score += 0
    elif 100 <= platelets < 150:
        sofa_score += 1
    elif 50 <= platelets < 100:
        sofa_score += 2
    elif 20 <= platelets < 50:
        sofa_score += 3
    else:
        sofa_score += 4

    # 3. Fígado (Bilirrubina)
    if bilirubin < 1.2:
        sofa_score += 0
    elif 1.2 <= bilirubin < 2.0:
        sofa_score += 1
    elif 2.0 <= bilirubin < 6.0:
        sofa_score += 2
    elif 6.0 <= bilirubin < 12.0:
        sofa_score += 3
    else:
        sofa_score += 4

    # 4. Sistema cardiovascular (MAP e uso de vasopressores)
    if map_value >= 70 and not vasopressor_use:
        sofa_score += 0
    elif map_value < 70 and not vasopressor_use:
        sofa_score += 1
    elif vasopressor_use:
        sofa_score += 2  # Dopamina ≤ 5 µg/kg/min ou dobutamina

    # 5. Sistema nervoso central (Escala de Coma de Glasgow)
    if gcs == 15:
        sofa_score += 0
    elif 13 <= gcs < 15:
        sofa_score += 1
    elif 10 <= gcs < 13:
        sofa_score += 2
    elif 6 <= gcs < 10:
        sofa_score += 3
    else:
        sofa_score += 4

    # 6. Função renal (Creatinina)
    if creatinine < 1.2:
        sofa_score += 0
    elif 1.2 <= creatinine < 2.0:
        sofa_score += 1
    elif 2.0 <= creatinine < 3.5:
        sofa_score += 2
    elif 3.5 <= creatinine < 5.0:
        sofa_score += 3
    else:
        sofa_score += 4

    return sofa_score
