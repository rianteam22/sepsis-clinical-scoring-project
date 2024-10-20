# app/calculators/omsofa.py

def calculate_omsofa(pao2_fio2, platelets, bilirubin, map_value, vasopressor_use, gcs, creatinine):
    omsofa_score = 0

    # 1. Respiração (PaO2/FiO2 ratio)
    if pao2_fio2 >= 400:
        omsofa_score += 0
    elif 300 <= pao2_fio2 < 400:
        omsofa_score += 1
    elif 200 <= pao2_fio2 < 300:
        omsofa_score += 2
    elif 100 <= pao2_fio2 < 200:
        omsofa_score += 3
    else:
        omsofa_score += 4

    # 2. Coagulação (Plaquetas)
    if platelets >= 150:
        omsofa_score += 0
    elif 100 <= platelets < 150:
        omsofa_score += 1
    elif 50 <= platelets < 100:
        omsofa_score += 2
    elif 20 <= platelets < 50:
        omsofa_score += 3
    else:
        omsofa_score += 4

    # 3. Fígado (Bilirrubina)
    if bilirubin < 1.2:
        omsofa_score += 0
    elif 1.2 <= bilirubin < 2.0:
        omsofa_score += 1
    elif 2.0 <= bilirubin < 6.0:
        omsofa_score += 2
    elif 6.0 <= bilirubin < 12.0:
        omsofa_score += 3
    else:
        omsofa_score += 4

    # 4. Cardiovascular (MAP e uso de vasopressores)
    if map_value >= 70 and not vasopressor_use:
        omsofa_score += 0
    elif map_value < 70 and not vasopressor_use:
        omsofa_score += 1
    elif vasopressor_use:
        omsofa_score += 2  # Vasopressores leves

    # 5. Sistema nervoso central (Glasgow Coma Scale)
    if gcs == 15:
        omsofa_score += 0
    elif 13 <= gcs < 15:
        omsofa_score += 1
    elif 10 <= gcs < 13:
        omsofa_score += 2
    elif 6 <= gcs < 10:
        omsofa_score += 3
    else:
        omsofa_score += 4

    # 6. Função renal (Creatinina)
    if creatinine < 1.2:
        omsofa_score += 0
    elif 1.2 <= creatinine < 2.0:
        omsofa_score += 1
    elif 2.0 <= creatinine < 3.5:
        omsofa_score += 2
    elif 3.5 <= creatinine < 5.0:
        omsofa_score += 3
    else:
        omsofa_score += 4

    return omsofa_score
