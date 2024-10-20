# app/calculators/omqsofa.py

def calculate_omqsofa(respiratory_rate, systolic_bp, gcs):
    omqsofa_score = 0

    # 1. Frequência respiratória ≥ 22 respirações/minuto
    if respiratory_rate >= 22:
        omqsofa_score += 1

    # 2. Pressão arterial sistólica ≤ 100 mmHg
    if systolic_bp <= 100:
        omqsofa_score += 1

    # 3. Alteração no estado mental (GCS < 15)
    if gcs < 15:
        omqsofa_score += 1

    return omqsofa_score
