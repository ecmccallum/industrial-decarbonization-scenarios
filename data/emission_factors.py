"""
emission_factors.py

ADEME Base Carbone v23 emission factors for French industrial sites.
Source: https://www.bilans-ges.ademe.fr/
Units: kgCO2eq per unit of activity (see comments for units)
Last updated: April 2026
"""

# ── SCOPE 1: Direct combustion on site ──────────────────────────────────────
# These are emissions your site produces directly by burning fuels on site.
# Unit: kgCO2eq per kWh of energy content (lower heating value)

SCOPE1 = {
    'natural_gas': 0.227,   # kgCO2eq / kWh
    'fuel_oil':    0.324,   # kgCO2eq / kWh
    'coal':        0.342,   # kgCO2eq / kWh
    'lpg':         0.275,   # kgCO2eq / kWh
    'diesel':      0.271,   # kgCO2eq / kWh (stationary use)
}

# ── SCOPE 2: Purchased electricity by country ────────────────────────────────
# Location-based method. French grid is low because of nuclear power.
# Unit: kgCO2eq per kWh of electricity purchased

SCOPE2_ELECTRICITY = {
    'FR':          0.052,   # France — nuclear-heavy grid
    'DE':          0.485,   # Germany — more coal and gas
    'EU_avg':      0.295,   # European average
    'UK':          0.233,   # United Kingdom
    'renewable_ppa': 0.005, # Renewable PPA — near zero
}

# ── BIOMETHANE: lifecycle carbon intensity by feedstock ──────────────────────
# Lower values = better. Biomethane from waste is near-zero or even negative.
# Different feedstocks have different biochemical methane potential (BMP)
# and different upstream emissions from collection and transport.
# Unit: kgCO2eq per MWh of biomethane energy content

BIOMETHANE = {
    'agricultural_waste': 23,   # kgCO2eq / MWh
    'food_waste':         18,   # kgCO2eq / MWh
    'sewage_sludge':      28,   # kgCO2eq / MWh
    'energy_crops':       45,   # kgCO2eq / MWh — less favourable
    'landfill_gas':       12,   # kgCO2eq / MWh — captured methane
}

# ── CHEMICALS: used in remediation and water treatment ───────────────────────
# Emission factors for chemical inputs used in the bioremediation module.
# These represent the carbon cost of producing each chemical industrially.
# Unit: kgCO2eq per kg of chemical produced

CHEMICALS = {
    'hydrogen_peroxide_kg':  0.635,  # kgCO2eq / kg H2O2
    'ferrous_sulfate_kg':    0.410,  # kgCO2eq / kg FeSO4
    'sulfuric_acid_kg':      0.175,  # kgCO2eq / kg H2SO4
    'sodium_persulfate_kg':  0.820,  # kgCO2eq / kg
    'activated_carbon_kg':   2.150,  # kgCO2eq / kg — high energy to produce
}

# ── LABORATORY INSTRUMENTS: energy consumption ───────────────────────────────
# Used in the analytical monitoring overhead module.
# Quantifies the carbon cost of running monitoring programmes.
# Source: manufacturer specifications and published laboratory energy audits.
# Unit: kWh per hour of instrument operation

INSTRUMENT_ENERGY_KWH_PER_HOUR = {
    'GC_FID':    0.5,   # gas chromatograph with FID detector
    'HPLC_UV':   0.3,   # HPLC with UV detector
    'IC':        0.4,   # ion chromatograph
    'AAS':       1.2,   # atomic absorption spectrometer
    'GC_MS':     0.8,   # GC-MS
    'autoclave': 2.0,   # sample sterilisation
    'fume_hood': 0.6,   # ventilation per running hour
}