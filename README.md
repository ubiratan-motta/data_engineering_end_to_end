# End-to-end Data Engineering Design.

### Data engineering is the process of creating the structure to store raw data so that it can be analyzed later. Taking care of the collection, preparation and governance of this data to ensure that it is at a good level of quality for modeling and visualization.

This repository will be used to exemplify how an ETL data engineering process works. Traditional data transformation process consisting of three steps: extracting, transforming and loading data. To do this, some different tools and technologies are used.

![image](https://user-images.githubusercontent.com/103541346/211004487-2b75368c-db42-4a9f-b434-053b4d7c2b90.png)

## In this project the technologies used will be:
- Python
- PySpark
- GCP
- AirFlow
- SQL
- JavaScript (Json)

Among other concepts that will be used to load the databases

#### Python and PySpark - The programming of the scripts will be done in Python together with the PySpark Framework, using several Python libraries.
#### GCP - The Data Warehouse will be GCP's BigQuery.
#### AirFlow - To automate the process, we will use an AirFlow DAG, so whenever new raw data arrives, the process will be automatically loaded in BgQuery.
#### JavaScript(Json) - Raw payload files are in Json and csv.
#### SQL - To check the quality of the data loaded into BigQuery we will use SQL to make the necessary queries.

## Final considerations
All data, Json, and csv files were developed by me. So it is a very extensive work and it takes a lot of time. This project aims to assist in the development and understanding of how the entire data engineering process works.

This project can be considered a continuation of these other two repositories:
- Ecomerce Database Logical Project: <https://github.com/ubiratan-motta/Projeto_Conceitual_Banco_de_Dados_E-Commerce>
- Ecomerce Database Conceptual Project: <https://github.com/ubiratan-motta/Projeto_L-gico_Banco_de_Dados_ECOMMERCE>

Whenever changes are made and commits to the project I will update the READme.
