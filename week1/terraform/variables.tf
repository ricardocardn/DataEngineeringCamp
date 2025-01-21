variable "CREDENTIALS" {
  description = "The path to the credentials file"
  type        = string
  default     = "./keys/creds.json"
}

variable "PROJECT_ID" {
  description = "The project ID"
  type        = string
  default     = "dataengineering-448518"
}

variable "BUCKET_NAME" {
  description = "The name of the bucket"
  type        = string
  default     = "dataengineering-2025"
}

variable "DATASET_ID" {
  description = "The dataset ID"
  type        = string
  default     = "dataengineeringdataset"
}

variable "LOCATION" {
  description = "The location of the elements"
  type        = string
  default     = "US-central1"
}