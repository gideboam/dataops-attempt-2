import subprocess

print("Starting ETL Pipeline...")

subprocess.run(["python3", "generate.py"], check=True)
subprocess.run(["python3", "transform.py"], check=True)
subprocess.run(["python3", "load.py"], check=True)

print("ETL Pipeline Completed Successfully!")
