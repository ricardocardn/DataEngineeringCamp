resource "google_storage_bucket" "bucket" {
  name          = var.BUCKET_NAME
  location      = var.LOCATION
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 3
    }

    action {
      type = "Delete"
    }
  }
}