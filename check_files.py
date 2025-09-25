import os

def check_file(path):
    """Check if file exists and not empty"""
    if os.path.isfile(path) and os.path.getsize(path) > 0:
        print(f"✅ {path} exists and not empty")
    else:
        print(f"❌ {path} missing or empty")

def check_directory(path):
    """Check if directory exists and not empty"""
    if os.path.isdir(path) and os.listdir(path):
        print(f"✅ {path} exists and not empty")
    else:
        print(f"❌ {path} missing or empty")

if __name__ == "__main__":
    check_file("alx_travel_app/requirement.txt")
    check_directory("alx_travel_app/listings")
    check_file("alx_travel_app/settings.py")
    check_file("alx_travel_app/urls.py")
