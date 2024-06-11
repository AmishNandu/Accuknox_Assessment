import psutil
import logging
import os
path=os.getcwd()
f=open('system_health.log', 'w')
f.close()
# Set up logging
logging.basicConfig(filename=path+'/system_health.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define thresholds
CPU_THRESHOLD = 80  # in percent
MEMORY_THRESHOLD = 80  # in percent
DISK_THRESHOLD = 80  # in percent


def log_alert(message):
    """Logs an alert message to the console and log file."""
    logging.warning(message)
    print(message)


def check_cpu_usage():
    """Checks CPU usage and logs an alert if it exceeds the threshold."""
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"High CPU usage detected: {cpu_usage}%")
    else:
        logging.info(f"CPU usage : {cpu_usage}%")

def check_memory_usage():
    """Checks memory usage and logs an alert if it exceeds the threshold."""
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        log_alert(f"High memory usage detected: {memory_usage}%")
    else:
        logging.info(f"Memory usage : {memory_usage}%")

def check_disk_usage():
    """Checks disk usage and logs an alert if it exceeds the threshold."""
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        log_alert(f"High disk usage detected: {disk_usage}%")
    else:
        logging.info(f"Disk usage : {disk_usage}%")

def check_running_processes():
    """Logs the count of running processes."""
    process_count = len(psutil.pids())
    logging.info(f"Running processes count: {process_count}")


def monitor_system_health():
    """Monitors system health and logs alerts if thresholds are exceeded."""
    logging.info("Starting system health check...")

    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()

    logging.info("System health check completed.")


if __name__ == "__main__":
    monitor_system_health()
