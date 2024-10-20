# app/calculators/qsofa.py

def calculate_qsofa(respiratory_rate, mentation_status, systolic_bp):
    qsofa_score = 0
    
    # Frequência respiratória ≥ 22 respirações/minuto
    if respiratory_rate >= 22:
        qsofa_score += 1

    # Alteração no estado mental
    if mentation_status == 1:  # 1 representa alteração no estado mental
        qsofa_score += 1

    # Pressão arterial sistólica ≤ 100 mmHg
    if systolic_bp <= 100:
        qsofa_score += 1

    return qsofa_score
