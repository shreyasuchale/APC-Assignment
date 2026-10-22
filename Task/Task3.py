# 3.	Write a program to design a configuration system for a web server where some configuration settings should not be changed during runtime, while others can be updated. The server settings are as follows:
# ●	server_ip: A tuple representing the IP address of the server, which should remain unchanged.
# ●	allowed_ips: A list of IP addresses allowed to connect to the server, which can be updated during runtime.
# Write a program that:
# ●	Allows updating the allowed_ips list.
# ●	Prevents updating the server_ip tuple.
# ●	Displays the updated configuration.
# Tasks:
# ●	Use a tuple for server_ip and a list for allowed_ips.
# ●	Implement a function to update allowed_ips but prevent changes to server_ip.


server_ip = ("192.168.1.100",)
allowed_ips = ["192.168.1.1", "192.168.1.2"]

def update_allowed_ip():
    ip = input("Enter New Allowed IP: ")
    allowed_ips.append(ip)
    print("Allowed IP Added Successfully.")

def display_configuration():

    print("\nServer Configuration")
    print("Server IP :", server_ip[0])
    print("Allowed IPs :", allowed_ips)

while True:

    print("\n MENU ")
    print("1. Add Allowed IP")
    print("2. Change Server IP")
    print("3. Display Configuration")
    print("4. Exit")

    choice = int(input("Enter Your Choice: "))

    match choice:

        case 1:
            update_allowed_ip()

        case 2:
            print("Server IP Cannot Be Changed (Tuple is Immutable).")

        case 3:
            display_configuration()

        case 4:
            print("Program Ended.")
            break

        case _:
            print("Invalid Choice!")
            
            
            
            
            
            
            