
resource "azurerm_resource_group" "rg" {
    count = 3 
    location = var.resource_group_location
    name = element(var.resource_group_name, count.index)
}