
# Homework

## **Question 1:** Understanding docker first run

To run the python image using Docker, you can use the following command:

```bash
docker run -it --entrypoint bash python:3.12.8
```

At first, Docker will probably failed to run the image because it is not downloaded yet (the image might not be available locally yet). In this case, Docker will download the image from Docker Hub and then run it. After the image is downloaded, you will be in the bash shell of the python image. The prompted result will be similar to the following:

```bash
~> docker run -it --entrypoint bash python:3.12.8
Unable to find image 'python:3.12.8' locally
3.12.8: Pulling from library/python
e474a4a4cbbf: Pull complete 
d22b85d68f8a: Pull complete 
936252136b92: Pull complete 
94c5996c7a64: Pull complete 
c980de82d033: Pull complete 
e05e1469c731: Pull complete 
ded9ddaf4f92: Pull complete 
Digest: sha256:5893362478144406ee0771bd9c38081a185077fb317ba71d01b7567678a89708
Status: Downloaded newer image for python:3.12.8
root@a354907f0f96:/# 
```

Now, to check the pip version, you can use the following command inside the bash shell container:

```bash
pip --version
```

The result, in January 2025, is the next one:

```bash
root@a354907f0f96:/# pip --version
pip 24.3.1 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)
```

ANSWER: The pip version is `24.3.1`.

## **Question 2:** Understanding Docker networking and docker-compose

If you want to access the postgres container by port 5432 from the host machine, you can use `localhost` as the hostname. However, if you plan to use the service within the context of a docker compose infrastructure, you should use the service name as the hostname. In this case, the service name is `db`, so that the hostname should be `db`. On the other hand, the port keeps the same value, `5432`.

In Figures 1 and 2 you may see how we will be able to create the connection between pgadmin and postgres using this hostname and port.

<p align="center">
<img width="70%" alt="image" src="https://github.com/user-attachments/assets/6451614e-0a2b-4a20-9eba-b825eda3302a" />
</p>
<p align="center"><b>Figure 1:</b> Creating connectiong between containers. Here, the postgres container is named pgdatabase instead of db.</p>

<p align="center">
<img width="70%" alt="Screenshot 2025-01-21 at 20 39 24" src="https://github.com/user-attachments/assets/0d62a6ad-8c99-4129-bd48-6ddafea47a20" />
</p>
<p align="center"><b>Figure 2:</b> Checking postgres database content</p>

(*) NOTE: to be able to use the postgres service directly from your host machine, you should first define a network, configure as `bridge`, and then attach the postgres service to this network. This way, you can access the postgres service by using the `localhost` hostname and the port `5432`. You can do the same thing to the other service.

ANSWER:
- Hostname: `db`
- Port: `5432`

## **Question 3:** Trip Segmentation Count

First, we'll need to retrieve the [Yellow Taxi Trip Records](https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2019-10.parquet) dataset corresponding to the month of October. This dataset is already partitioned by month on the website, making it the only way to acquire the data for a specific period. Therefore, filtering by date using WHERE clauses may not be necessary. However, I have attempted to load additional data into the database to demonstrate the effectiveness of this filtering technique. You can check how this data was ingested on the `data_ingestion.ipynb` notebook.

The SQL prompt to form such a query looks like the following:

```sql
SELECT 
    SUM(CASE WHEN trip_distance <= 1 THEN 1 ELSE 0 END) AS up_to_1_mile,
    SUM(CASE WHEN trip_distance > 1 AND trip_distance <= 3 THEN 1 ELSE 0 END) AS between_1_and_3_miles,
    SUM(CASE WHEN trip_distance > 3 AND trip_distance <= 7 THEN 1 ELSE 0 END) AS between_3_and_7_miles,
    SUM(CASE WHEN trip_distance > 7 AND trip_distance <= 10 THEN 1 ELSE 0 END) AS between_7_and_10_miles,
    SUM(CASE WHEN trip_distance > 10 THEN 1 ELSE 0 END) AS over_10_miles
FROM taxi_2019 as t
WHERE t."tpep_pickup_datetime" >= '2019-10-01' 
  AND t."tpep_pickup_datetime" < '2019-11-01';
```

Where `taxi_2019` is the table that only contains data from 2019. The following result was obtained:

<p align="center">
<img width="70%" alt="image" src="https://github.com/user-attachments/assets/81823a3a-22da-47a1-ae2f-64ef4353a956" />
</p>
<p align="center"><b>Figure 3:</b> SQL Statement Result</p>

ANSWER: 104,802; 198,924; 109,603; 27,678; 35,189


## **Question 4:** Longest trip for each day

To obtain the asked information, we should run the next sql statement.

```sql
SELECT 
	DATE(tpep_pickup_datetime) as date,
	MAX(trip_distance) as distance
from taxi_2019
GROUP by date
ORDER by distance DESC
LIMIT 1;
```

This led us to the result in Figure 4.

<p align="center">
<img width="70%" alt="image" src="https://github.com/user-attachments/assets/66558754-7eb8-420b-af83-cd219dfe9cf4" />
</p>
<p align="center"><b>Figure 4:</b> SQL Statement Result</p>

ANSWER: 2019-10-31

## **Question 5:** Three biggest pickup zones

The SQL statement is:

```sql
SELECT 
    z."Zone", 
    DATE(t.lpep_pickup_datetime) AS pickup_date,
    SUM(t.total_amount) AS total_amount_sum
FROM 
    taxi_2019 AS t
JOIN 
    zones AS z
ON 
    t."PULocationID" = z."LocationID"
WHERE 
    DATE(t.lpep_pickup_datetime) = '2019-10-18'
GROUP BY 
    z."Zone", DATE(t.lpep_pickup_datetime)
HAVING 
    SUM(t.total_amount) > 13000
ORDER BY 
    total_amount_sum DESC;
```

ANSWER: 
- East Harlem North
- East Harlem South
- Morningside Heights

## **Question 6:** Largest tip

The SQL statement is:

```sql
SELECT z2."Zone" as doZone, MAX(t."tip_amount") as Largest_tip
FROM taxi_2019 as t, zones as z1, zones as z2
WHERE t."PULocationID" = z1."LocationID" AND
	z1."Zone" = 'East Harlem North' AND
	t."DOLocationID" = z2."LocationID"
GROUP BY z2."Zone"
ORDER BY Largest_tip DESC
LIMIT 1;
```

<p align="center">
<img width="70%" alt="image" src="https://github.com/user-attachments/assets/7291b290-7997-4c89-8dcd-5a2df676ddd8" />
</p>
<p align="center"><b>Figure 5:</b> SQL Statement Result</p>

ANSWER: JFK Airport with a tip of 87 dollars

## **Question 7:** Terraform Workflow

ANSWER: terraform init, terraform apply -auto-approve, terraform destroy
