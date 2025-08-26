import matplotlib.pyplot as plt
import pandas as pd

def read_json_to_dataframe(input_file):
    # Read in the data from a JSON file into pandas df
    eva_df = pd.read_json(input_file, convert_dates=['date'])
    eva_df['eva'] = eva_df['eva'].astype(float)
    # clean the data by removing incomplete rows and sorting by date
    eva_df.dropna(axis=0, inplace=True)
    eva_df.sort_values('date', inplace=True)
    return eva_df

def write_dataframe_to_csv(df, output_file):
    # Save data frame to CSV file for later analysis
    df.to_csv(output_file, index=False)

# Data source: https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r', encoding='ascii')
output_file = open('./eva-data.csv', 'w', encoding='utf-8')
graph_file = './cumulative_eva_graph.png'

eva_data = read_json_to_dataframe(input_file)

write_dataframe_to_csv(eva_data, output_file)

# Plot cumulative time spent in space over years
eva_data['duration_hours'] = eva_data['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
eva_data['cumulative_time'] = eva_data['duration_hours'].cumsum()
plt.plot(eva_data['date'], eva_data['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()
