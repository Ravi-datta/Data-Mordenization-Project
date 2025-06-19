# Data Modernization Project

**A turnkey data modernization proof-of-concept for migrating mortgage servicing data from a CTW-style legacy system to a Snowflake Nexus-style platform, showcasing end-to-end profiling, mapping, and migration planning using Excel, SQL, and Python.**

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Repository Structure](#repository-structure)
4. [Prerequisites](#prerequisites)
5. [Getting Started](#getting-started)
6. [Project Deliverables](#project-deliverables)
7. [Usage Examples](#usage-examples)
8. [Agile Artifacts](#agile-artifacts)
9. [Reporting & Automation](#reporting--automation)
10. [Contributing](#contributing)
11. [License](#license)

---

## Overview
This project simulates a real-world data modernization engagement in a mortgage servicing context. It demonstrates:
- **Business analysis**: Defining scope, stakeholder requirements, and acceptance criteria.
- **Data profiling**: Identifying quality issues (nulls, outliers) in legacy CTW tables via Excel pivot tables.
- **Data mapping**: Field-by-field mapping to Snowflake Nexus tables with SQL transformation logic.
- **Migration planning**: Phased ETL/ELT strategy with rollback and reconciliation procedures.
- **Agile delivery**: User stories, sprint plans, and retrospectives to drive incremental delivery.
- **Automation**: Python scripts to generate profiling and mapping reports.

## Features
- Interactive Excel templates for project charter, data inventory, profiling, and mapping
- SQL scripts for extracting samples and validating transformations in Snowflake
- Python utility for automating report generation and documentation updates
- PowerPoint decks outlining migration strategy and stakeholder presentations
- Agile artifacts (user stories, sprint planning, retrospectives) in Excel

## Repository Structure
```
MyMortgageDataModernizationProject/
├── README.md                # This documentation file
├── docs/
│   ├── 01_Project_Charter.xlsx
│   ├── 02_Data_Inventory.xlsx
│   ├── 03_Data_Profiling_Report.xlsx
│   ├── 04_Data_Mapping_Template.xlsx
│   ├── 05_Agile_Artifacts/
│   │   ├── 05A_User_Stories.xlsx
│   │   ├── 05B_Sprint_Planning.xlsx
│   │   └── 05C_Retrospectives.xlsx
│   ├── 06_Migration_Strategy.pptx
│   └── 07_Stakeholder_Presentation.pptx
├── sql/
│   ├── source_data_queries.sql
│   └── mapping_views.sql
├── python/
│   └── generate_docs.py
└── deliverables/
    └── samples/
        ├── sample_profile_output.csv
        └── sample_mapped_view.csv
```

## Prerequisites
- Microsoft Excel (for templates and pivot charts)
- Snowflake account or compatible SQL environment
- Python 3.7+ with pandas
- Git

## Getting Started
1. **Clone the repo**
   ```bash
git clone https://github.com/YourUsername/MyMortgageDataModernizationProject.git
cd MyMortgageDataModernizationProject
```
2. **Populate Legacy Sample Data**
   - Load provided sample CSVs into your CTW-like schema.
3. **Run Profiling Queries**
   ```sql
-- In Snowflake (or equivalent)
SOURCE @sql/source_data_queries.sql;
```
4. **Review Profiling Report**
   - Open `docs/03_Data_Profiling_Report.xlsx` in Excel to analyze null counts, distributions, and anomalies.
5. **Validate Mappings**
   ```sql
SOURCE @sql/mapping_views.sql;
SELECT * FROM vw_validated_loans;
```
6. **Automate Report Updates**
   ```bash
python python/generate_docs.py
```
7. **Review Agile Artifacts**
   - Open stories, sprint planning, and retrospective files under `docs/05_Agile_Artifacts/`.
8. **Present to Stakeholders**
   - Use PowerPoint decks in `docs/06_Migration_Strategy.pptx` and `docs/07_Stakeholder_Presentation.pptx`.

## Project Deliverables
- **Charter**: Scope, objectives, timeline, risks
- **Inventory**: Catalog of 50+ legacy tables and columns
- **Profiling Report**: Null counts, distinct values, histograms
- **Mapping Template**: Field mappings with transformation logic
- **SQL Scripts**: Sample extraction & mapping validation views
- **Migration Strategy**: Phased ETL/ELT plan slides
- **Agile Artifacts**: User stories, sprint plans, retrospectives
- **Automation**: Python script for report generation
- **Presentations**: Stakeholder-ready slide decks

## Usage Examples
- Quickly spot data quality issues by refreshing the profiling report with new samples.
- Validate transformation logic in Snowflake by querying the mapping views.
- Iterate on user stories and sprint artifacts to align with changing requirements.

## Agile Artifacts
- **User Stories**: Define business needs (e.g., "As an analyst, I want consistent loan IDs...")
- **Sprint Planning**: Track backlog, capacity, and burndown charts
- **Retrospectives**: Document lessons learned and continuous improvements

## Reporting & Automation
- Automated profiling summary in Excel via `python/generate_docs.py`.
- Sample outputs in `deliverables/samples/` for reference.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for enhancements or bug fixes.

## License
MIT © Your Name
