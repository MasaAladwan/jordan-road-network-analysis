# Jordan Road Network Analysis

This project analyzes Jordan's road network using Social Network Analysis (SNA) techniques to identify important intersections and understand traffic flow patterns.

## Project Overview

The analysis focuses on:
1. Finding important intersections using centrality metrics
2. Understanding traffic flow patterns
3. Identifying critical nodes in the road network

### Key Questions Answered
- Which intersections are well connected?
- Which intersections are closest to all others?
- Which intersections act as critical bridges in traffic flow?

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/jordan-road-network-analysis.git
cd jordan-road-network-analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Dependencies

The project uses the following main libraries:
- OSMnx: For accessing and processing OpenStreetMap data
- NetworkX: For network analysis
- Pandas: For data manipulation
- Matplotlib: For visualization
- GeoPandas: For geospatial data handling

## Project Structure

```
.
├── README.md
├── requirements.txt
├── notebooks/
│   └── road_network_analysis.ipynb
├── data/
│   ├── jordan_nodes_centrality.csv
│   ├── jordan_edges.csv
│   ├── jordan_nodes_centrality.shp
│   └── jordan_edges.shp
└── results/
    └── visualizations/
```

## Usage

1. Open the Jupyter notebook:
```bash
jupyter notebook notebooks/road_network_analysis.ipynb
```

2. Run the analysis cells to:
   - Download and process the road network
   - Calculate centrality metrics
   - Generate visualizations
   - Export results

## Results

The analysis produces:
- Centrality metrics for intersections
- Network visualizations
- Geographic data files (CSV and Shapefile formats)

## License


## Contributing

