import subprocess
import platform

def show_popup():
    """Displays a pop-up message using PowerShell or cmd."""
    if platform.system() == "Windows":
        try:
            # Try using PowerShell first
            subprocess.run(["powershell", "-Command", "[System.Windows.MessageBox]::Show('Hello', 'Popup')"], check=True)
        except Exception:
            # Fallback to cmd's msg command
            subprocess.run(["msg", "*", "Hello"], check=True)
    else:
        print("This script is for Windows only!")

if __name__ == "__main__":
    show_popup()
