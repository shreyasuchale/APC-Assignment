# Web Server Configuration Management System

# Server IP is stored as a tuple and should not be changed
server_ip = (192, 168, 1, 10)

# Allowed IP addresses are stored in a list and can be updated
allowed_ips = ["192.168.1.20", "192.168.1.30"]


# Function to update allowed IPs
def update_allowed_ips(new_ip):
    if new_ip not in allowed_ips:
        allowed_ips.append(new_ip)
        print(new_ip, "has been added to allowed IPs.")
    else:
        print(new_ip, "is already in the allowed IP list.")


# Function to display configuration
def display_configuration():
    print("\n--- Web Server Configuration ---")
    print("Server IP:", ".".join(map(str, server_ip)))
    print("Allowed IPs:", allowed_ips)


# Function to prevent changing server IP
def update_server_ip(new_ip):
    print("Error: server_ip cannot be changed during runtime.")
    print("The server IP remains:", ".".join(map(str, server_ip)))


# Display original configuration
print("Original Configuration:")
display_configuration()


# Update allowed IP
print("\nUpdating allowed IP...")
new_ip = input("Enter new IP address to allow: ")
update_allowed_ips(new_ip)


# Try to update server IP
print("\nTrying to update server IP...")
new_server_ip = (10, 0, 0, 1)
update_server_ip(new_server_ip)


# Display updated configuration
print("\nUpdated Configuration:")
display_configuration()