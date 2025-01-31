import re


#sample log file 
log_file = "./data/auth.log"


# Pattern to match failed login attemps
failed_login_pattern = r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)"

def analyze_logs(log_file):
    with open(log_file,"r") as file:
        for line in file:
            match = re.search(failed_login_pattern,line)
            if match:
                print(f"Failed login attemp from IP: {match.group(1)}")

analyze_logs(log_file)