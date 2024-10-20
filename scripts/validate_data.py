def validate_data(row):
    # Colunas reais para infecção e sepse
    required_columns = [
        'TAX_infecção', 'PAM_infecção', 'FC_infecção', 'FR_infecção', 'ECGlasgow_infecção', 'Cr_infecção',
        'TAX_sepse', 'PAM_sepse', 'FC_sepse', 'FR_sepse', 'ECGlasgow_sepse', 'Cr_sepse'
    ]

    # Verificar se todas as colunas necessárias estão presentes
    for column in required_columns:
        if pd.isnull(row[column]):
            print(f"Coluna ausente: {column}")
            return False

    # Validação de faixas para colunas específicas
    if not (30 <= row['TAX_infecção'] <= 45) or not (30 <= row['TAX_sepse'] <= 45):
        print("Temperatura fora da faixa aceitável.")
        return False
    if not (20 <= row['PAM_infecção'] <= 200) or not (20 <= row['PAM_sepse'] <= 200):
        print("PAM fora da faixa aceitável.")
        return False
    if not (0 <= row['FC_infecção'] <= 200) or not (0 <= row['FC_sepse'] <= 200):
        print("Frequência cardíaca fora da faixa aceitável.")
        return False
    if not (0 <= row['FR_infecção'] <= 60) or not (0 <= row['FR_sepse'] <= 60):
        print("Frequência respiratória fora da faixa aceitável.")
        return False
    if not (0 <= row['Cr_infecção'] <= 15) or not (0 <= row['Cr_sepse'] <= 15):
        print("Creatinina fora da faixa aceitável.")
        return False
    if not (3 <= row['ECGlasgow_infecção'] <= 15) or not (3 <= row['ECGlasgow_sepse'] <= 15):
        print("GCS fora da faixa aceitável.")
        return False

    return True
