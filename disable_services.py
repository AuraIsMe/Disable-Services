import subprocess
import sys
import ctypes

def is_admin():
    """Check if the script is running with administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    """Restart the script with administrative privileges."""
    try:
        if sys.version_info[0] == 3 and sys.version_info[1] >= 5:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
    except Exception as e:
        print(f"Failed to elevate privileges: {e}")
        sys.exit(1)
      
services_to_disable = [
    "SysMain",             # Superfetch
    "WSearch",             # Windows Search
    "DiagTrack",           # Diagnostic Tracking Service
    "DoSvc",               # Delivery Optimization
    "Fax",                 # Fax
    "WMPNetworkSvc",       # Windows Media Player Network Sharing Service
    "XblGameSave",         # Xbox Live Game Save
    "XboxNetApiSvc",       # Xbox Live Networking Service
    "RetailDemo",          # Retail Demo Service
    "MapsBroker",          # Downloaded Maps Manager
    "dmwappushservice",    # Device Management Wireless Application Protocol (WAP) Push message Routing Service
    "PrintNotify",         # Printer Extensions and Notifications
    "RemoteRegistry",      # Remote Registry
    "TrkWks",              # Distributed Link Tracking Client
    "Fax",                 # Fax
    "bthserv",             # Bluetooth Support Service
]

def disable_service(service_name):
    try:
        subprocess.run(["sc", "config", service_name, "start= disabled"], check=True)
        subprocess.run(["sc", "stop", service_name], check=True)
        print(f"Service {service_name} disabled and stopped successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to disable or stop {service_name}: {e}")

def main():
    if not is_admin():
        print("This script needs to be run with administrative privileges. Restarting as admin...")
        run_as_admin()
        sys.exit(0)
    else:
        for service in services_to_disable:
            disable_service(service)

if __name__ == "__main__":
    main()
