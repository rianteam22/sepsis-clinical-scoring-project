# calculate_scores.py
import pandas as pd
from calculators.qsofa import calculate_qsofa
from calculators.sofa import calculate_sofa
from calculators.sirs import calculate_sirs
from calculators.apache_ii import calculate_apache_ii
from calculators.mods import calculate_mods
from calculators.mews import calculate_mews
from calculators.sos import calculate_sos
from calculators.omqsofa import calculate_omqsofa
from calculators.omsofa import calculate_omsofa
from calculators.saps_3 import calculate_saps_3

def process_csv(input_file, output_file):
    # Carregar o CSV em um DataFrame
    df = pd.read_csv(input_file)

    # Iterar por cada linha (paciente) e calcular os escores
    for index, row in df.iterrows():
        # Verificar se os dados de infecção estão presentes
        infection_data_present = pd.notna(row['FR_infecção']) and pd.notna(row['PAS_infecção']) and pd.notna(row['ECGlasgow_infecção'])
        sepsis_data_present = pd.notna(row['FR_sepse']) and pd.notna(row['PAS_sepse']) and pd.notna(row['ECGlasgow_sepse'])

        if infection_data_present:
            respiratory_rate_infection = row['FR_infecção']
            systolic_bp_infection = row['PAS_infecção']
            altered_mentation_infection = 1 if row['ECGlasgow_infecção'] < 15 else 0  # Alteração no estado mental
            
            # Calcular qSOFA para infecção
            qsofa_infection = calculate_qsofa(respiratory_rate_infection, altered_mentation_infection, systolic_bp_infection)
            df.at[index, 'qSOFA_infecção'] = qsofa_infection

            # Cálculo do SOFA para infecção
            sofa_infection = calculate_sofa(
                row['PaO2/FiO2_infecção'], row['Plaquetas_infecção'], row['Bilirrubina_infecção'],
                row['PAM_infecção'], row['Vasopressor_infecção'], row['ECGlasgow_infecção'], row['Cr_infecção']
            )
            df.at[index, 'SOFA_infecção'] = sofa_infection

            # Cálculo do SIRS para infecção
            sirs_infection = calculate_sirs(
                row['TAX_infecção'], row['FC_infecção'], row['FR_infecção'],
                row['Leucócitos_infecção'], row.get('pCO2_infecção', None), row.get('Bastonetes_infecção', None)
            )
            df.at[index, 'SIRS_infecção'] = sirs_infection

            # Calcular APACHE II para infecção
            apache_ii_infection = calculate_apache_ii(
                row['TAX_infecção'], row['PAM_infecção'], row['FC_infecção'], row['FR_infecção'],
                row['pH_infecção'], row['Na_infecção'], row['K_infecção'], row['Cr_infecção'],
                row['Ht_infecção'], row['Leucócitos_infecção'], row['ECGlasgow_infecção'], row['Idade'], row['Comorbidade']
            )
            df.at[index, 'APACHE_II_infecção'] = apache_ii_infection

            # Calcular SAPS 3 para infecção
            saps_3_infection = calculate_saps_3(
                row['Idade'], row['Comorbidade'], row['Tempo_internação_hospital'], 
                row['FC_infecção'], row['PAS_infecção'], row['PaO2/FiO2_infecção'],
                row['Ventilação_mecânica_infecção'], row['TAX_infecção'], row['Leucócitos_infecção'],
                row['Plaquetas_infecção'], row['pH_infecção'], row['Cr_infecção'], row['Bilirrubina_infecção']
            )
            df.at[index, 'SAPS_3_infecção'] = saps_3_infection

            # Calcular MODS para infecção
            mods_infection = calculate_mods(
                row['PaO2/FiO2_infecção'], row['Cr_infecção'], row['Bilirrubina_infecção'],
                row['PAM_infecção'], row['Vasopressor_infecção'], row['Plaquetas_infecção'], row['ECGlasgow_infecção']
            )
            df.at[index, 'MODS_infecção'] = mods_infection

            # Calcular MEWS para infecção
            mews_infection = calculate_mews(
                row['FR_infecção'], row['FC_infecção'], row['PAS_infecção'],
                row['TAX_infecção'], row['AVPU_infecção']
            )
            df.at[index, 'MEWS_infecção'] = mews_infection

            # Calcular SOS para infecção
            sos_infection = calculate_sos(
                row['TAX_infecção'], row['PAS_infecção'], row['FC_infecção'], 
                row['FR_infecção'], row['SatO2_infecção'], row['Leucócitos_infecção'], row['Lactato_infecção']
            )
            df.at[index, 'SOS_infecção'] = sos_infection

            # Calcular omqSOFA para infecção
            omqsofa_infection = calculate_omqsofa(
                row['FR_infecção'], row['PAS_infecção'], row['ECGlasgow_infecção']
            )
            df.at[index, 'omqSOFA_infecção'] = omqsofa_infection

            # Calcular omSOFA para infecção
            omsofa_infection = calculate_omsofa(
                row['PaO2/FiO2_infecção'], row['Plaquetas_infecção'], row['Bilirrubina_infecção'],
                row['PAM_infecção'], row['Vasopressor_infecção'], row['ECGlasgow_infecção'], row['Cr_infecção']
            )
            df.at[index, 'omSOFA_infecção'] = omsofa_infection



        if sepsis_data_present:
            respiratory_rate_sepsis = row['FR_sepse']
            systolic_bp_sepsis = row['PAS_sepse']
            altered_mentation_sepsis = 1 if row['ECGlasgow_sepse'] < 15 else 0  # Alteração no estado mental

            # Calcular qSOFA para sepse
            qsofa_sepsis = calculate_qsofa(respiratory_rate_sepsis, altered_mentation_sepsis, systolic_bp_sepsis)
            df.at[index, 'qSOFA_sepse'] = qsofa_sepsis
            
            # Cálculo do SOFA para sepse
            sofa_sepsis = calculate_sofa(
                row['PaO2/FiO2_sepse'], row['Plaquetas_sepse'], row['Bilirrubina_sepse'],
                row['PAM_sepse'], row['Vasopressor_sepse'], row['ECGlasgow_sepse'], row['Cr_sepse']
            )
            df.at[index, 'SOFA_sepse'] = sofa_sepsis

            # Cálculo do SIRS para sepse
            sirs_sepsis = calculate_sirs(
                row['TAX_sepse'], row['FC_sepse'], row['FR_sepse'],
                row['Leucócitos_sepse'], row.get('pCO2_sepse', None), row.get('Bastonetes_sepse', None)
            )
            df.at[index, 'SIRS_sepse'] = sirs_sepsis

            # Calcular APACHE II para sepse
            apache_ii_sepsis = calculate_apache_ii(
                row['TAX_sepse'], row['PAM_sepse'], row['FC_sepse'], row['FR_sepse'],
                row['pH_sepse'], row['Na_sepse'], row['K_sepse'], row['Cr_sepse'],
                row['Ht_sepse'], row['Leucócitos_sepse'], row['ECGlasgow_sepse'], row['Idade'], row['Comorbidade']
            )
            df.at[index, 'APACHE_II_sepse'] = apache_ii_sepsis

            # Calcular SAPS 3 para sepse
            saps_3_sepsis = calculate_saps_3(
                row['Idade'], row['Comorbidade'], row['Tempo_internação_hospital'], 
                row['FC_sepse'], row['PAS_sepse'], row['PaO2/FiO2_sepse'],
                row['Ventilação_mecânica_sepse'], row['TAX_sepse'], row['Leucócitos_sepse'],
                row['Plaquetas_sepse'], row['pH_sepse'], row['Cr_sepse'], row['Bilirrubina_sepse']
            )
            df.at[index, 'SAPS_3_sepse'] = saps_3_sepsis

            # Calcular MODS para sepse
            mods_sepsis = calculate_mods(
                row['PaO2/FiO2_sepse'], row['Cr_sepse'], row['Bilirrubina_sepse'],
                row['PAM_sepse'], row['Vasopressor_sepse'], row['Plaquetas_sepse'], row['ECGlasgow_sepse']
            )
            df.at[index, 'MODS_sepse'] = mods_sepsis

            # Calcular MEWS para sepse
            mews_sepsis = calculate_mews(
                row['FR_sepse'], row['FC_sepse'], row['PAS_sepse'],
                row['TAX_sepse'], row['AVPU_sepse']
            )
            df.at[index, 'MEWS_sepse'] = mews_sepsis

            # Calcular SOS para sepse
            sos_sepsis = calculate_sos(
                row['TAX_sepse'], row['PAS_sepse'], row['FC_sepse'], 
                row['FR_sepse'], row['SatO2_sepse'], row['Leucócitos_sepse'], row['Lactato_sepse']
            )
            df.at[index, 'SOS_sepse'] = sos_sepsis

            # Calcular omqSOFA para sepse
            omqsofa_sepsis = calculate_omqsofa(
                row['FR_sepse'], row['PAS_sepse'], row['ECGlasgow_sepse']
            )
            df.at[index, 'omqSOFA_sepse'] = omqsofa_sepsis

            # Calcular omSOFA para sepse
            omsofa_sepsis = calculate_omsofa(
                row['PaO2/FiO2_sepse'], row['Plaquetas_sepse'], row['Bilirrubina_sepse'],
                row['PAM_sepse'], row['Vasopressor_sepse'], row['ECGlasgow_sepse'], row['Cr_sepse']
            )
            df.at[index, 'omSOFA_sepse'] = omsofa_sepsis

    # Salvar o DataFrame atualizado em um novo arquivo CSV
    df.to_csv(output_file, index=False)
