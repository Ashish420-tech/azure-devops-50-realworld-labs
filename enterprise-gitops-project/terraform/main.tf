################################
# Resource Group
################################
resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}

################################
# Virtual Network
################################
resource "azurerm_virtual_network" "vnet" {
  name                = "vnet-enterprise"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}

################################
# Subnet
################################
resource "azurerm_subnet" "subnet" {
  name                 = "subnet-enterprise"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = ["10.0.1.0/24"]
}

################################
# Network Security Group
################################
resource "azurerm_network_security_group" "nsg" {
  name                = "nsg-enterprise"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name

  security_rule {
    name                       = "Allow-SSH"
    priority                   = 100
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "22"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
}
################################
# Attach NSG to Subnet
################################
resource "azurerm_subnet_network_security_group_association" "nsg_assoc" {
  subnet_id                 = azurerm_subnet.subnet.id
  network_security_group_id = azurerm_network_security_group.nsg.id
}
################################
# Network Interface (NIC)
################################
resource "azurerm_network_interface" "nic" {
  name                = "nic-enterprise"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.subnet.id
    private_ip_address_allocation = "Dynamic"
  }
}
################################
# Linux Virtual Machine (SAFE)
################################
resource "azurerm_linux_virtual_machine" "vm" {
  count               = var.create_vm ? 1 : 0
  name                = "vm-enterprise-devops"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  size                = "Standard_A1_v2"
  admin_username      = var.admin_username

  network_interface_ids = [
    azurerm_network_interface.nic.id
  ]

  admin_ssh_key {
    username   = var.admin_username
    public_key = file("~/.ssh/id_rsa.pub")
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts"
    version   = "latest"
  }

  depends_on = [
    azurerm_network_interface.nic
  ]
}
