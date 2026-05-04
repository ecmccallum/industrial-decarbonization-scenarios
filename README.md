# Industrial Decarbonization Scenario Modeller

A Python-based scenario modelling tool for quantifying Scope 1 and Scope 2
GHG emissions of energy-intensive industrial sites and simulating
decarbonization trajectories under multiple intervention levers.

---

## Project Status

| Module | Status |
|---|---|
| `data/emission_factors.py` — verified emission factor library | ✅ Complete |
| `data/sites.py` — site configuration dictionaries | ✅ Complete |
| `notebooks/01_baseline.ipynb` — Scope 1 and 2 baseline calculator | ✅ Complete |
| `notebooks/02_scenarios.ipynb` — decarbonization scenario simulator | ✅ Complete |
| `notebooks/03_trajectory.ipynb` — 2024–2050 trajectory builder | ✅ Complete |
| `notebooks/04_bioremediation.ipynb` — bioremediation vs Fenton comparison | ✅ Complete |
| `notebooks/05_biomethane.ipynb` — biomethane lifecycle by feedstock | ✅ Complete |
| `notebooks/06_lacq_case_study.ipynb` — full Lacq pipeline | ✅ Complete |
| `notebooks/07_monitoring_overhead.ipynb` — analytical monitoring carbon cost | ✅ Complete |
| `notebooks/08_visualisations.ipynb` — waterfall and trajectory charts | ✅ Complete |

---

## Project Overview

This repository demonstrates an end-to-end environmental data pipeline built
in Python, from raw emission factor data through to professional decarbonization
roadmaps and visualisations. It is structured around a real industrial context —
the Lacq petrochemical basin in Nouvelle-Aquitaine, France — and incorporates
experimental data from peer-reviewed research conducted at IPREM CNRS UMR 5254.

**What the tool does:**
- Calculates Scope 1 and 2 GHG emissions for any industrial site configuration
- Models four decarbonization levers individually and in combination
- Builds year-by-year emissions trajectories aligned with EU climate targets
- Compares the carbon footprint of bacterial bioremediation vs chemical oxidation
- Analyses biomethane feedstock lifecycle intensity using BMP data
- Quantifies the carbon overhead of analytical monitoring programmes

---

## Key Results

### Lacq baseline — 211,550 tCO2eq/year

| Source | tCO2eq | % of total |
|---|---|---|
| Natural gas combustion (Scope 1) | 181,600 | 85.8% |
| Fuel oil combustion (Scope 1) | 16,200 | 7.7% |
| Purchased electricity (Scope 2) | 13,750 | 6.5% |

Natural gas combustion dominates at 85.8%. The French nuclear grid
(0.055 kgCO2eq/kWh) makes Scope 2 almost irrelevant — renewable PPA saves
only 5.3% of total emissions even at 100% adoption. Biomethane substitution
at 40% saves 30.9%. CCS on residual Scope 1 at 90% capture saves 84.2%.

### Grid comparison — why geography matters

| Grid | EF (kgCO2eq/kWh) | Lacq Scope 2 (tCO2eq) |
|---|---|---|
| France (FR_2023) | 0.055 | 13,750 |
| United Kingdom | 0.225 | 56,250 |
| EU average | 0.255 | 63,750 |
| Germany (DE_2023) | 0.380 | 95,000 |
| Renewable PPA | 0.010 | 2,500 |

Lacq's Scope 2 would be 6.9x higher on the German grid. This demonstrates
why PPA is a priority lever in Germany but largely irrelevant in France —
decarbonization strategy is geography-dependent.

### Decarbonization trajectory 2024–2050

![Waterfall chart](outputs/lacq_waterfall.png)

![Trajectory](outputs/lacq_trajectory.png)

Under the modelled deployment plan (100% PPA by 2030, 40% biomethane by 2030,
CCS from 2035), Lacq reaches 94.1% reduction by 2035. The EU Fit for 55
2030 target is missed by 39,822 tCO2eq under a realistic deployment timeline
— biomethane adoption would need to accelerate or partial CCS be introduced
earlier to close the gap.

### Bioremediation vs Fenton chemical oxidation

| | Bioremediation | Fenton |
|---|---|---|
| Carbon footprint (kgCO2eq/m3) | 0.132 | 0.606 |
| Full site — 2,000 m3 (tCO2eq) | 0.264 | 1.211 |
| Hexadecane removal | 97.24% | 90.0% |
| Phenanthrene removal | 63.44% | 80.0% |

Bioremediation is 78% lower carbon than Fenton for a hexadecane-dominated
site. Fenton outperforms on phenanthrene removal due to hydroxyl radical
reactivity toward aromatic ring structures. The dominant cost in Fenton is
embodied carbon from hydrogen peroxide production (0.52 kgCO2eq/m3).

### Analytical monitoring overhead

Annual carbon footprint of a 12-month GC-FID and HPLC-UV monitoring
programme: **261 kgCO2eq/year**. Transport accounts for 94% of this total.
Monitoring overhead equals 27.5% of the carbon saved by choosing bioremediation
over Fenton — switching sample collection to an electric vehicle would reduce
this to approximately 7%.

---

## Scientific and Industrial Context

| Lever | Scope | Mechanism | Lacq result at stated adoption |
|---|---|---|---|
| Renewable PPA 100% | Scope 2 | Replace grid electricity | −11,250 tCO2eq (5.3%) |
| Biomethane 40% | Scope 1 | Replace natural gas | −65,280 tCO2eq (30.9%) |
| CCS 90% on Scope 1 | Scope 1 | Capture and store CO2 | −178,020 tCO2eq (84.2%) |

---

## Methods

**Python stack:** pandas, numpy, matplotlib

**Emission factors by category:**

| Category | Source |
|---|---|
| Scope 1 combustion (LHV basis) | ADEME Base Empreinte V23.6, July 2025 |
| Scope 2 — France | ADEME Base Empreinte V23.6 / RTE Annual Electricity Review 2023 |
| Scope 2 — Germany | Umweltbundesamt (UBA), 2024 |
| Scope 2 — EU average | European Environment Agency (EEA), 2024 edition |
| Scope 2 — United Kingdom | UK Dept. for Energy Security and Net Zero (DESNZ), 2024 |
| Scope 2 — renewable PPA | ecoinvent v3.10 (infrastructure and manufacturing only) |
| Chemicals embodied carbon | ecoinvent v3.10, cradle-to-gate |
| Biomethane lifecycle intensity | ADEME Base Empreinte V23.6 and peer-reviewed LCA literature |
| Laboratory instrument energy | Manufacturer datasheets, Agilent ACT-label 2023, My Green Lab audits |

**Regulatory references:** EU Fit for 55, EU CSRD, GHG Protocol Corporate Standard

Scope 1 formula (LHV basis, MWh × kgCO2eq/kWh = tCO2eq):

    E = Activity (MWh) × Emission factor (kgCO2eq/kWh)

Scope 2 formula (location-based):

    E = Electricity (MWh) × Grid emission factor (kgCO2eq/kWh)

**Biomethane lifecycle carbon intensity by feedstock:**

| Feedstock | kgCO2eq/kWh | BMP (Nm3/tVS) | Best yield |
|---|---|---|---|
| Agricultural waste | 0.023 | 280 | |
| Food waste | 0.018 | 450 | ✓ highest yield |
| Sewage sludge | 0.028 | 220 | |
| Energy crops | 0.045 | 340 | |
| Landfill gas | 0.012 | n/a | ✓ lowest carbon |

---

## Data Note

Site energy consumption values are illustrative, based on published
TotalEnergies Nouvelle-Aquitaine reporting ranges and IEA French petrochemical
sector benchmarks (IEA, 2023). All emission factors are version-tagged for
auditability and traceable to primary sources. The pipeline accepts real site
energy audit data without structural changes.

The bioremediation module uses experimental degradation data from Gulumbe et al.
(2025), conducted at IPREM CNRS UMR 5254 under supervision of Prof. Robert Duran.

---

## References

Gulumbe, B.H., Cravo-Laureau, C. & Duran, R. (2025). Integrative genomic
and transcriptomic analyses reveal marine *Actinomycetota* adaptations for
hydrocarbon degradation. *Environmental Technology & Innovation*, 40, 104361.
https://doi.org/10.1016/j.eti.2025.104361

ADEME (2025). Base Empreinte V23.6 — Facteurs d'émissions de référence.
https://data.ademe.fr/datasets/base-carboner

Umweltbundesamt (2024). CO2-Emissionsfaktor fur den Strommix in Deutschland 2023.

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

LinkedIn: https://linkedin.com/in/ecmccallum
GitHub: https://github.com/ecmccallum