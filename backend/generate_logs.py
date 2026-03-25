import random
import csv
import time
from datetime import datetime

LOG_FILE = "backend/sample_data/log_data.log"

log_levels = ["INFO", "ERROR", "WARN", "DEBUG"]
log_weights = [0.7, 0.1, 0.15, 0.05]

services = ["auth", "payment", "inventory", "shipping", "user", "orders", "notifications", "analytics", "search", "recommendation"]

info_msgs = ["Request processed successfully", "User logged in", "Data retrieved", "Operation completed",
             "Cache hit", "Cache list", "Connection established", "Transaction completed", "Email sent", "Notification delivered"]

error_msgs = ["Database connection failed", "Timeout occurred", "Null pointer exception", "Out of memory",
              "Service unavailable", "Failed to process request", "Unauthorized access attempt",
              "Data validation error", "Disk full", "API rate limit exceeded"]

# Write header
with open(LOG_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "service", "level", "message"])

print("Generating log data...")

i = 0

while True:
    i += 1

    # 🔥 FORCE anomaly after 50 logs
    if i > 50:
        level = "ERROR"
        service = "auth"
    else:
        level = random.choices(log_levels, weights=log_weights)[0]
        service = random.choice(services)

    # message selection
    if level == "ERROR":
        message = random.choice(error_msgs)
    else:
        message = random.choice(info_msgs)

    # 🔥 IMPORTANT: SAME MINUTE GROUPING
    fixed_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    timestamp = f"{fixed_time}:00"

    row = [
        timestamp,
        service,
        level,
        message
    ]

    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)

    time.sleep(0.1)