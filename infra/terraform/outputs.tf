output "public_ip" {
  description = "Публічна IP-адреса сервера для доступу до застосунку"
  value       = azurerm_linux_virtual_machine.main.public_ip_address
}