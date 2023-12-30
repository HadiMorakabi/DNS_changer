import tkinter as tk
import os

def get_active_network_interface():
    try:
        # Run 'netsh interface show interface' command to get the active network interface
        result = os.popen('netsh interface show interface').read()
        for line in result.splitlines():
            if "Connected" in line:
                return line.split("  ")[-1]
    except Exception as e:
        print(f"Error: {e}")
        return None

def set_dns(ip_address):
    network_name = get_active_network_interface()
    if network_name is None:
        print("your device is not connectedto any network")
        return
    try:
        # Change DNS settings using netsh command
        os.system('netsh interface ip set dns ' + f'"{network_name}"' + ' static ' + ip_address)
        print("DNS set to " + ip_address)
    except Exception as e:
        print(f"Error: {e}")

def set_dns_automatic():
    network_name = get_active_network_interface()
    if network_name is None:
        print("your device is not connectedto any network")
        return
    try:
        # Set DNS to automatic using netsh command
        os.system('netsh interface ip set dns ' + f'"{network_name}"' + ' dhcp')
        print("DNS set to automatic")
    except Exception as e:
        print(f"Error: {e}")

# define a function to get the current dns settings
def get_dns():
    network_name = get_active_network_interface()
    if network_name is None:
        print("your device is not connectedto any network")
        return
    try:
        # Run 'netsh interface ip show config' command to get the current DNS settings
        result = os.popen('netsh interface ip show config ' + f'"{network_name}"').read()
        for line in result.splitlines():
            if "DNS servers configured through DHCP" in line:
                return "Automatic"
            if "Statically Configured DNS Servers" in line:
                return line.split(":")[-1].strip()
    except Exception as e:
        print(f"Error: {e}")
        return None

# Create the main window
window = tk.Tk()
window.title("DNS Settings Changer")
#change the size of the window
window.geometry("400x200")
#
# Function to handle button clicks
def button_click(ip_address=None):
    if ip_address is not None:
        set_dns(ip_address)
    else:
        set_dns_automatic()

# Create buttons
btn_dns1 = tk.Button(window, text="Set DNS to google", command=lambda: button_click("8.8.8.8"))
btn_dns2 = tk.Button(window, text="Set DNS to shecan", command=lambda: button_click("178.22.122.100"))
btn_automatic = tk.Button(window, text="Set DNS to Automatic", command=lambda: button_click())
btn_show_dns = tk.Button(window, text="Show DNS", command=lambda: print("your currnet dns ip address is: ",get_dns()))

label = tk.Label(window, text="by: Mohamad Hadi Morakabi\nEmail: mh.me220@gmail.com", font=("Arial Bold", 10), fg="red")
label.pack(side=tk.BOTTOM)
# Pack buttons into the window
btn_dns1.pack(side=tk.RIGHT,padx=10,pady=10)
btn_dns2.pack(side=tk.LEFT,padx=10,pady=10)
btn_automatic.pack(side=tk.BOTTOM,pady=30)
btn_show_dns.pack(side=tk.BOTTOM,pady=10)

# Run the GUI loop
window.mainloop()
