provider "google" {
  credentials = "${file("account.json")}"
  project     = "selenium-1220"
  region      = "europe-west1"
}
