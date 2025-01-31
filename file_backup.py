import shutil
from datetime import datetime


# Source and destination directories
source_dir = "./data/critical"
backup_dir = f"./backups/{datetime.now().strftime("%Y%m%d_%H%M%S")}"


# Create backup
shutil.copytree(source_dir,backup_dir)
print(f"Backup created at: {backup_dir}")
