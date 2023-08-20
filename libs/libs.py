import subprocess
import pkg_resources

def check_installed(package_name):
    return package_name in {dist.project_name for dist in pkg_resources.working_set}

def install_codrone_edu_library():
    if check_installed('codrone-edu'):
        print("CoDrone Edu library is already installed.")
        # log_installed_packages()
    else:
        try:
            subprocess.check_call(['pip', 'install', 'codrone-edu'])
            print("CoDrone Edu library installed successfully.")
        except subprocess.CalledProcessError:
            print("Error installing CoDrone Edu library.")

def log_installed_packages():
    installed_packages = [dist.project_name for dist in pkg_resources.working_set]
    print("Installed packages:")
    for package in installed_packages:
        print(package)


