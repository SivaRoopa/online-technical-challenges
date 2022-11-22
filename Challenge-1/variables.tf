variable "resource_group_location" {
  default     = "eastus"
  description = "Location of the resource group."
}

  variable "resource_group_name" {
  description = "Default resource group name that the network will be created in."
  #type        = list
  default     = ["dev-rg","qa-rg", "prof-rg"]

}