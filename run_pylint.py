import subprocess
import os

TARGET = "backend/app"
REPORT_DIR = "backend/reports"
REPORT_PATH = os.path.join(REPORT_DIR, "pylint_report.txt")

# Create report directory if not exists
os.makedirs(REPORT_DIR, exist_ok=True)

print(f"🔍 Running pylint on: {TARGET}")
result = subprocess.run(
    ["pylint", TARGET],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
)

# Save output
with open(REPORT_PATH, "w", encoding="utf-8") as f:
    f.write(result.stdout)

# Extract and display score
for line in result.stdout.splitlines():
    if "Your code has been rated at" in line:
        print("📊", line)
        score = float(line.split("/")[0].split()[-1])
        if score >= 8.0:
            print("✅ Passed: Pylint score is >= 8.0")
        else:
            print("❌ Failed: Pylint score is below 8.0")
        break
