resource "google_bigquery_dataset" "dataset" {
  dataset_id = var.DATASET_ID
  project    = var.PROJECT_ID
  location   = var.LOCATION
}