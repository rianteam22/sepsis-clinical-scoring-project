# app/calculators/mods.py

def calculate_mods(pao2_fio2, creatinine, bilirubin, map_value, vasopressor_use, platelets, gcs):
    mods_score = 0

    # 1. Respiratório (PaO₂/FiO₂ Ratio)
    if pao2_fio2 >= 300:
        mods_score += 0
    elif 200 <= pao2_fio2 < 300:
        mods_score += 1
    elif 100 <= pao2_fio2 < 200:
        mods_score += 3
    else:
        mods_score += 4

    # 2. Renal (Creatinina)
    if creatinine < 1.2:
        mods_score += 0
    elif 1.2 <= creatinine < 2.0:
        mods_score += 1
    elif 2.0 <= creatinine < 3.5:
        mods_score += 2
    elif 3.5 <= creatinine < 5.0:
        mods_score += 3
    else:
        mods_score += 4

    # 3. Hepático (Bilirrubina)
    if bilirubin < 1.2:
        mods_score += 0
    elif 1.2 <= bilirubin < 2.0:
        mods_score += 1
    elif 2.0 <= bilirubin < 6.0:
        mods_score += 2
    elif 6.0 <= bilirubin < 12.0:
        mods_score += 3
    else:
        mods_score += 4

    # 4. Cardiovascular (MAP e uso de vasopressores)
    if map_value >= 70 and not vasopressor_use:
        mods_score += 0
    elif map_value < 70 and not vasopressor_use:
        mods_score += 1
    elif vasopressor_use:
        mods_score += 3  # Para uso de vasopressores leves

    # 5. Hematológico (Plaquetas)
    if platelets >= 120:
        mods_score += 0
    elif 80 <= platelets < 120:
        mods_score += 1
    elif 50 <= platelets < 80:
        mods_score += 2
    elif 20 <= platelets < 50:
        mods_score += 3
    else:
        mods_score += 4

    # 6. Neurológico (GCS)
    if gcs == 15:
        mods_score += 0
    elif 13 <= gcs < 15:
        mods_score += 1
    elif 10 <= gcs < 13:
        mods_score += 2
    elif 6 <= gcs < 10:
        mods_score += 3
    else:
        mods_score += 4

    return mods_score
