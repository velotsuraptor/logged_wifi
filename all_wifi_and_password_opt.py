import subprocess
import sys
meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
data = meta_data.decode('utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(':')[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear'])
        results = results.decode('utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print("{:<30}| {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30}| {:<}".format(i, ""))
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving password for {i}: {e}")
    except Exception as e:
        print(f"An error occurred for {i}: {e}")
