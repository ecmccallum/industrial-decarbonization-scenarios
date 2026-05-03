# Industrial Decarbonization Scenario Modeller

A Python-based scenario modelling tool for quantifying Scope 1 and Scope 2
GHG emissions of energy-intensive industrial sites and simulating
decarbonization trajectories under multiple intervention levers.

---

## Project Overview

This repository demonstrates an end-to-end environmental data pipeline:

- Scope 1 and 2 emissions calculation using ADEME Base Empreinte V23.6 factors
- Scenario modelling — renewable PPA, biomethane, electrification, CCS
- Bioremediation vs chemical treatment carbon footprint comparison
- Biomethane lifecycle carbon intensity analysis by feedstock with BMP data
- Decarbonization trajectory visualisation toward 2030 and 2050 targets
- Analytical monitoring carbon overhead quantification

The tool accepts any industrial site configuration and produces reproducible,
auditable decarbonization roadmaps.

---

## Project Status

| Module | Status |
|---|---|
| `data/emission_factors.py` — verified emission factor library | ✅ Complete |
| `data/sites.py` — site configuration dictionaries | ✅ Complete |
| `notebooks/01_baseline.ipynb` — Scope 1 and 2 baseline calculator | ✅ Complete |
| `notebooks/02_scenarios.ipynb` — decarbonization scenario simulator | 🔄 In progress |
| `notebooks/03_trajectory.ipynb` — 2024–2050 trajectory builder | 🔄 In progress |
| `notebooks/04_bioremediation.ipynb` — bioremediation vs Fenton comparison | 🔄 In progress |
| `notebooks/05_biomethane.ipynb` — biomethane lifecycle by feedstock | 🔄 In progress |
| `notebooks/06_lacq_case_study.ipynb` — full Lacq pipeline | 🔄 In progress |
| `notebooks/07_monitoring_overhead.ipynb` — analytical monitoring carbon cost | 🔄 In progress |
| `notebooks/08_visualisations.ipynb` — waterfall and trajectory charts | 🔄 In progress |

---

## Scientific and Industrial Context

Decarbonization of energy-intensive industries requires simultaneous
evaluation of multiple intervention levers, each with distinct carbon
reduction potential, cost profile, and implementation timeline.

| Lever | Scope targeted | Mechanism | Typical reduction |
|---|---|---|---|
| Renewable electricity PPA | Scope 2 | Replace grid electricity | Up to 95% of Scope 2 |
| Biomethane substitution | Scope 1 | Replace natural gas | 10–90% of gas emissions |
| Process electrification | Scope 1 + 2 | Convert thermal to electric | Site-dependent |
| CCS on residual emissions | Scope 1 | Capture and store CO2 | Up to 90% of residual |

This project models these levers individually and in combination, producing
waterfall abatement charts and trajectory plots aligned with EU climate targets.

A unique module compares the carbon footprint of bacterial bioremediation
versus Fenton chemical oxidation for hydrocarbon-contaminated coastal marine
sites, using experimental degradation data from Gulumbe, Cravo-Laureau &
Duran (2025) as the foreground inventory.

**Illustrative case study — Lacq petrochemical site, Nouvelle-Aquitaine:**
- Baseline Scope 1 + 2: 212,000 tCO₂eq/year
- Natural gas combustion: 85.8% of total emissions
- Purchased electricity: 6.5% of total (French nuclear grid, 0.055 kgCO₂eq/kWh)
- Sector benchmark: French gas processing sector average (IEA 2023)
- 2030 target: −55% under EU Fit for 55
- 2050 target: net zero

---

## Key Finding — Baseline Analysis

Natural gas combustion dominates at 85.8% of total Scope 1 and 2 emissions.
The French nuclear-heavy electricity grid (0.055 kgCO₂eq/kWh) means Scope 2
represents only 6.5% of the total footprint. This makes renewable PPA a weak
lever at Lacq — fuel switching and biomethane substitution are the priority
interventions.

---

## Methods

**Python stack:**
- pandas — data structures and tabular outputs
- numpy — numerical calculations
- matplotlib — scientific visualisation

**Emission factors by category:**

| Category | Source |
|---|---|
| Scope 1 combustion (LHV basis) | ADEME Base Empreinte V23.6, July 2025 |
| Scope 2 electricity — France | ADEME Base Empreinte V23.6 / RTE Annual Electricity Review 2023 |
| Scope 2 electricity — Germany | Umweltbundesamt (UBA), 2024 |
| Scope 2 electricity — EU average | European Environment Agency (EEA), 2024 edition |
| Scope 2 electricity — United Kingdom | UK Dept. for Energy Security and Net Zero (DESNZ), 2024 |
| Scope 2 — renewable PPA | ecoinvent v3.10 (infrastructure and manufacturing only) |
| Chemicals embodied carbon | ecoinvent v3.10, cradle-to-gate |
| Biomethane lifecycle intensity | ADEME Base Empreinte V23.6 and peer-reviewed LCA literature |
| Laboratory instrument energy | Manufacturer datasheets, Agilent ACT-label 2023, My Green Lab / UCSC green-lab audits |

**Regulatory references:** EU Fit for 55, EU CSRD, GHG Protocol Corporate Standard

Scope 1 — direct combustion emissions (LHV basis):

    E = Activity (MWh) × Emission factor (kgCO₂eq/kWh) / 1000

Scope 2 — purchased electricity, location-based method:

    E = Electricity (MWh) × Grid emission factor (kgCO₂eq/kWh) / 1000

Biomethane lifecycle carbon intensity by feedstock (kgCO₂eq/kWh, LHV):

| Feedstock | kgCO₂eq/kWh |
|---|---|
| Agricultural waste | 0.023 |
| Food waste | 0.018 |
| Sewage sludge | 0.028 |
| Energy crops | 0.045 |
| Landfill gas | 0.012 |

---

## Data Note

Site energy consumption values are illustrative, based on published
TotalEnergies Nouvelle-Aquitaine reporting ranges and IEA French petrochemical
sector benchmarks (IEA, 2023). All emission factors are version-tagged for
auditability and traceable to primary sources.

The bioremediation module uses experimental degradation data from
Gulumbe et al. (2025), conducted at IPREM CNRS UMR 5254 under supervision
of corresponding author Prof. Robert Duran.

This pipeline is designed to accept real site energy audit data without
structural changes.

---

## Why This Project Matters

This project demonstrates the ability to translate industrial energy
consumption data into actionable decarbonization roadmaps using reproducible
Python workflows.

It reflects:

- Quantitative environmental assessment of industrial systems
- Understanding of EU climate policy and carbon accounting methodology
- Integration of bioremediation science into carbon footprint analysis
- Clear communication of complex multi-lever scenarios

These skills are directly transferable to carbon consulting, industrial
sustainability analysis, and environmental project management roles.

---

## References

Gulumbe, B.H., Cravo-Laureau, C. & Duran, R. (2025). Integrative genomic
and transcriptomic analyses reveal marine *Actinomycetota* adaptations for
hydrocarbon degradation. *Environmental Technology & Innovation*, 40, 104361.
https://doi.org/10.1016/j.eti.2025.104361

ADEME (2025). Base Empreinte V23.6 — Facteurs d'émissions de référence.
https://data.ademe.fr/datasets/base-carboner

Umweltbundesamt (2024). CO₂-Emissionsfaktor für den Strommix in Deutschland 2023.

UK Department for Energy Security and Net Zero (2024). GHG Conversion Factors
for Company Reporting 2024.

European Environment Agency (2024). GHG Emission Intensity of Electricity
Generation in Europe.

RTE (2023). Annual Electricity Review 2023.

IEA (2023). France Energy Policy Review. International Energy Agency.

European Commission (2021). Fit for 55 package — EU climate targets for 2030.

---

## Author

Emma McCallum
Université de Pau et des Pays de l'Adour

LinkedIn: https://linkedin.com/in/ecmccallum
GitHub: https://github.com/ecmccallum