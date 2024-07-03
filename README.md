# Windows 10 Services Disabler

This script disables certain Windows 10 services to improve system performance by reducing the number of background processes.

## Prerequisites

- Python 3.5 or higher must be installed on your system.

## Usage

    The script will automatically prompt you for administrative privileges using the User Account Control (UAC) dialog. Once you grant permission, it will restart itself with elevated permissions to disable the specified services.

## List of Disabled Services

The script disables the following services:

- SysMain (Superfetch)
- WSearch (Windows Search)
- DiagTrack (Diagnostic Tracking Service)
- DoSvc (Delivery Optimization)
- Fax
- WMPNetworkSvc (Windows Media Player Network Sharing Service)
- XblGameSave (Xbox Live Game Save)
- XboxNetApiSvc (Xbox Live Networking Service)
- RetailDemo (Retail Demo Service)
- MapsBroker (Downloaded Maps Manager)
- dmwappushservice (Device Management Wireless Application Protocol (WAP) Push message Routing Service)
- PrintNotify (Printer Extensions and Notifications)
- RemoteRegistry (Remote Registry)
- TrkWks (Distributed Link Tracking Client)
- bthserv (Bluetooth Support Service)

## Important Notes

- **Backup your system** before running the script.
- **Test in a non-production environment** if possible to ensure that disabling these services does not affect your workflow.
- Some services may be necessary for certain applications, so adjust the list based on your specific needs.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Disclaimer

Use this script at your own risk. The author is not responsible for any damage that may occur from using this script.

