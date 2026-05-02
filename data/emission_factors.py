"""
emission_factors.py
Carbon intensity factors for environmental and remediation modelling.

Sources:
    [ADEME]  ADEME Base Empreinte® V23.6 (July 2025) — Scope 1 combustion,
             French electricity, biomethane lifecycle values.
             https://data.ademe.fr/datasets/base-carboner
    [UBA]    Umweltbundesamt (German Federal Environment Agency), 2024.
             CO₂-Emissionsfaktor für den Strommix in Deutschland 2023.
    [DESNZ]  UK Dept. for Energy Security and Net Zero, 2024.
             UK Government GHG Conversion Factors for Company Reporting 2024.
    [RTE]    RTE Réseau de Transport d'Électricité, Annual Electricity Review 2023.
    [EEA]    European Environment Agency, GHG Emission Intensity of
             Electricity Generation in Europe, 2024 edition.
    [EI]     ecoinvent v3.10 — chemicals, upstream LCA.
    [LIT]    Peer-reviewed literature / ADEME studies — biomethane,
             instrument energy.

All electricity factors are location-based (average grid mix) unless stated
otherwise. Fuel factors are on a lower heating value (LHV / PCI) basis,
consistent with ADEME reporting convention.

Last updated: May 2026
"""

# ── SCOPE 1: Direct combustion ────────────────────────────────────────────────
# Source: ADEME Base Empreinte V23.6
# Unit:   kgCO₂eq / kWh PCI (LHV)
# Includes CO₂, CH₄, N₂O as CO₂eq (GWP100, AR5).
# Scope 1 combustion only — upstream extraction/transport not included.
SCOPE1 = {
    'natural_gas': 0.227,   # [ADEME]
    'fuel_oil':    0.324,   # [ADEME] fioul domestique
    'coal':        0.342,   # [ADEME] houille
    'lpg':         0.274,   # [ADEME]
    'diesel':      0.267,   # [ADEME] stationary use
}

# ── SCOPE 2: Electricity — location-based average grid mix ───────────────────
# Unit: kgCO₂eq / kWh electricity consumed (consumption-based, includes imports)
SCOPE2_ELECTRICITY = {
    'FR_2023':       0.055,  # France — ADEME Base Empreinte V23.6 / RTE 2023
                              # Nuclear-dominated; consumption-based ~55 gCO₂eq/kWh
    'DE_2023':       0.380,  # Germany — Umweltbundesamt [UBA] 2024 (2023 data)
    'EU_avg_2023':   0.255,  # EU-27 average — EEA 2024 edition [EEA]
    'UK_2023':       0.225,  # UK — DESNZ 2024; generation + T&D combined [DESNZ]
    'renewable_ppa': 0.010,  # LCA estimate — infrastructure & manufacturing only [EI]
}

# ── BIOMETHANE: lifecycle carbon intensity ────────────────────────────────────
# Source: ADEME Base Empreinte V23.6 + peer-reviewed LCA literature [LIT]
# Unit:   kgCO₂eq / kWh (energy content of biomethane, LHV basis)
# Scope:  feedstock collection, pre-treatment, anaerobic digestion, upgrading,
#         compression, fugitive CH₄ leakage. Grid injection assumed.
#         Excludes avoided landfill/combustion credits (conservative).
BIOMETHANE = {
    'agricultural_waste': 0.023,   # [ADEME / LIT]
    'food_waste':         0.018,   # [ADEME / LIT]
    'sewage_sludge':      0.028,   # [ADEME / LIT]
    'energy_crops':       0.045,   # [ADEME / LIT] — higher due to land-use & fertiliser
    'landfill_gas':       0.012,   # [LIT] — highly variable (±50 %) with collection efficiency
}

# ── CHEMICALS: embodied carbon (cradle-to-gate) ───────────────────────────────
# Source: ecoinvent v3.10 [EI]; cross-checked with ADEME Base Empreinte
# Unit:   kgCO₂eq / kg (as supplied)
CHEMICALS = {
    'hydrogen_peroxide':  0.65,  # 50 wt% aq. solution [EI: hydrogen peroxide, RoW]
    'ferrous_sulfate':    0.41,  # FeSO₄·7H₂O, by-product of TiO₂ production [EI]
    'sulfuric_acid':      0.18,  # 98 % H₂SO₄, contact process [EI: sulfuric acid, RoW]
    'sodium_persulfate':  0.82,  # Na₂S₂O₈ [EI, approximated; ±20 % uncertainty]
    'activated_carbon':   2.10,  # Coal-based GAC [EI: activated carbon, GLO]
                                  # Range: ~1.5 (coconut shell) to 4.8 (coal) kgCO₂eq/kg
                                  # Use feedstock-specific value where known
}

# ── LABORATORY INSTRUMENTS: energy intensity (active run state) ───────────────
# Source: manufacturer datasheets, Agilent ACT-label measurements,
#         My Green Lab / UCSC green-lab audits [LIT]
# Unit:   kWh / hour of active operation (not idle/standby)
# Idle power is typically 30–60 % of run power.
# Convert to emissions via SCOPE2_ELECTRICITY factors.
INSTRUMENT_ENERGY_KWH_PER_HOUR = {
    'GC_FID':    0.50,  # Benchtop GC, temperature-programmed; ~400–600 W [LIT]
    'HPLC_UV':   0.55,  # Agilent 1260 Infinity II (pump + detector + thermostat)
                         # ACT-label: ~4.2 kWh/8-hr day ≈ 0.52 kWh/hr run state [LIT]
    'IC':        0.40,  # e.g. Thermo Dionex ICS-2100; ~350–450 W run state [LIT]
    'AAS':       1.20,  # Flame AAS (air-acetylene); ~900–1400 W [LIT]
    'GC_MS':     0.80,  # Benchtop GC-MS incl. turbomolecular + fore-pump [LIT]
    'autoclave': 2.00,  # Bench-top steam autoclave 50–100 L; averaged over full cycle [LIT]
    'fume_hood': 1.80,  # Standard ducted CAV hood (1.2 m); HVAC load ~1.5–2.0 kW [LIT]
                         # Use 0.60 kWh/hr for modern VAV (variable air volume) hoods
}