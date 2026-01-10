variable "location" {
 description = "Azure region"
 type 	     = string
 }
 
variable "resource_group_name" {

description = "Resource group name"
type        = string
}
variable "create_vm" {
  description = "Whether to create the virtual machine"
  type        = bool
  default     = true
}

variable "admin_username" {
  description = "Admin username for VM"
  type        = string
  default     = "azureuser"
}
 
