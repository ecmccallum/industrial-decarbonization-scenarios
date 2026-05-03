"""
sites.py
Site configuration dictionaries for industrial decarbonization modelling.

All energy values in MWh per year unless stated otherwise.
Data sources noted per site.

Last updated: May 2026
"""
# ── SITE 1: Lacq Gas Processing, Nouvelle-Aquitaine ──────────────────────────
# TotalEnergies operates the Lacq industrial basin near Pau.
# Values are illustrative, based on published TotalEnergies
# Sustainability Report 2023 ranges for Nouvelle-Aquitaine sites.
LACQ = {
    'name':               'Lacq Gas Processing Site (illustrative)',
    'sector':             'petrochemical',
    'location':           'Nouvelle-Aquitaine, France',
    'grid':               'FR_2023',
    'electricity_MWh':    250_000,
    'natural_gas_MWh':    800_000,
    'fuel_oil_MWh':        50_000,
    'employees':               850,
    'production_tonnes':   500_000,
    'note': 'Lacq basin, TotalEnergies Nouvelle-Aquitaine',
}
# ── SITE 2: French Cement Plant ───────────────────────────────────────────────
# Cement has both energy AND process emissions (calcination of limestone).
# This makes it analytically interesting for Scope 1 decomposition.
# Values are illustrative, benchmarked against French cement sector data.
CEMENT_PLANT = {
    'name':               'French Cement Plant (illustrative)',
    'sector':             'cement',
    'location':           'France',
    'grid':               'FR_2023',
    'electricity_MWh':    180_000,
    'natural_gas_MWh':    600_000,
    'coal_MWh':           200_000,
    'fuel_oil_MWh':        30_000,
    'process_tCO2':       450_000,   # calcination: CaCO3 -> CaO + CO2
    'employees':               600,
    'production_tonnes': 1_000_000,
    'note': 'Illustrative values, French cement sector benchmark',
}
# ── SITE 3: Contaminated coastal marine site ──────────────────────────────────
# Based on experimental conditions of Gulumbe et al. (2025).
# Your supervisor's paper — this is the direct data connection to your internship.
# Reference: Gulumbe, Cravo-Laureau & Duran (2025), ET&I; 40:104361
CONTAMINATED_SITE = {
    'name':                    'Coastal marine contaminated site (illustrative)',
    'area_m2':                        5_000,
    'volume_m3':                      2_000,
    'hexadecane_mg_L':                   50,   # initial concentration
    'phenanthrene_mg_L':                 50,   # initial concentration
    'target_removal_pct':                90,   # remediation target
    # Degradation data from Gulumbe et al. (2025)
    'bio_hexadecane_removal':         97.24,   # % removed in 12 days
    'bio_phenanthrene_removal':       63.44,   # % removed in 12 days
    'note': 'Gulumbe, Cravo-Laureau & Duran (2025), IPREM CNRS UMR 5254',
}

# ── All sites as a list for easy looping ─────────────────────────────────────
ALL_SITES = [LACQ, CEMENT_PLANT]