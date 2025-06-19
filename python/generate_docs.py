import pandas as pd
# Load sample CSVs
df_profile = pd.read_csv('../deliverables/samples/sample_profile_output.csv')
summary = df_profile.agg({'NullCount':'sum','DistinctValues':'count'})
summary.to_excel('../docs/03_Data_Profiling_Report.xlsx', sheet_name='Summary')