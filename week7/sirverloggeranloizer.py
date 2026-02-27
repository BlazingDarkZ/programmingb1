import re
import logging
import os
from collections import defaultdict, Counter

# Folder where the log file is located
log_dir = "C:/Users/S/Documents/GitHub/azure-appointment-app/programmingb1/week7"
os.makedirs(log_dir, exist_ok=True)

# Path to the log file
log_file_path = os.path.join(log_dir, "server.log.txt")

# Set up logging to go into the same folder
log_path = os.path.join(log_dir, "analysis_audit.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler()
    ]
)


class LogAnalyzer:

    def __init__(self, log_file):
        self.log_file = log_file
        self.log_pattern = re.compile(
            r'(\S+) - - \[(.*?)\] "(\S+) (\S+) \S+" (\d+) (\d+)'
        )

        self.total_requests = 0
        self.unique_ips = set()
        self.http_methods = Counter()
        self.urls = Counter()
        self.status_codes = Counter()
        self.errors = []

        self.failed_logins = defaultdict(list)
        self.forbidden_access = []
        self.security_incidents = []

    def parse_log_line(self, line):
        match = self.log_pattern.match(line)
        if not match:
            return None

        ip, timestamp, method, url, status, size = match.groups()

        return {
            "ip": ip,
            "timestamp": timestamp,
            "method": method,
            "url": url,
            "status": int(status),
            "size": int(size)
        }

    def analyze_security(self, entry):

        if entry["url"] == "/login" and entry["status"] == 401:
            self.failed_logins[entry["ip"]].append(entry["timestamp"])

            if len(self.failed_logins[entry["ip"]]) >= 3:
                incident = (
                    f"Brute force attempt from {entry['ip']} "
                    f"- {len(self.failed_logins[entry['ip']])} failed attempts"
                )
                self.security_incidents.append(incident)
                logging.warning(incident)

        if entry["status"] == 403:
            incident = (
                f"Forbidden access: {entry['ip']} -> {entry['url']}"
            )
            self.forbidden_access.append(incident)
            self.security_incidents.append(incident)
            logging.warning(incident)

        sql_patterns = ["union", "select", "drop", "insert", "--", ";"]
        url_lower = entry["url"].lower()

        if any(pattern in url_lower for pattern in sql_patterns):
            incident = (
                f"Possible SQL injection: {entry['ip']} -> {entry['url']}"
            )
            self.security_incidents.append(incident)
            logging.warning(incident)

    def process_logs(self):
        try:
            logging.info(f"Analyzing {self.log_file}")

            with open(self.log_file, "r") as file:
                for line_number, line in enumerate(file, 1):

                    entry = self.parse_log_line(line.strip())
                    if not entry:
                        continue

                    self.total_requests += 1
                    self.unique_ips.add(entry["ip"])
                    self.http_methods[entry["method"]] += 1
                    self.urls[entry["url"]] += 1
                    self.status_codes[entry["status"]] += 1

                    if entry["status"] >= 400:
                        self.errors.append(entry)

                    self.analyze_security(entry)

            logging.info(f"Finished: {self.total_requests} requests processed")

        except FileNotFoundError:
            logging.error("Log file not found")
            raise

        except PermissionError:
            logging.error("Permission denied")
            raise

    def generate_summary_report(self):
        report_path = os.path.join(log_dir, "summary_report.txt")
        try:
            with open(report_path, "w") as file:
                file.write("=" * 60 + "\n")
                file.write("SERVER LOG SUMMARY\n")
                file.write("=" * 60 + "\n\n")

                file.write(f"Total Requests: {self.total_requests}\n")
                file.write(f"Unique Visitors: {len(self.unique_ips)}\n\n")

                file.write("HTTP Methods:\n")
                for method, count in self.http_methods.most_common():
                    file.write(f"{method}: {count}\n")

                file.write("\nTop 5 URLs:\n")
                for url, count in self.urls.most_common(5):
                    file.write(f"{url}: {count}\n")

                file.write("\nStatus Codes:\n")
                for status, count in sorted(self.status_codes.items()):
                    file.write(f"{status}: {count}\n")

            logging.info("Summary report created")

        except PermissionError:
            logging.error("Cannot write summary report")

    def generate_security_report(self):
        report_path = os.path.join(log_dir, "security_incidents.txt")
        try:
            with open(report_path, "w") as file:
                file.write("=" * 60 + "\n")
                file.write("SECURITY REPORT\n")
                file.write("=" * 60 + "\n\n")

                file.write(f"Total Incidents: {len(self.security_incidents)}\n\n")

                file.write("Brute Force Attempts:\n")
                for ip, attempts in self.failed_logins.items():
                    if len(attempts) >= 3:
                        file.write(f"{ip}: {len(attempts)} failed logins\n")

                file.write("\nForbidden Access:\n")
                for incident in self.forbidden_access:
                    file.write(f"{incident}\n")

                file.write("\nAll Incidents:\n")
                for incident in self.security_incidents:
                    file.write(f"{incident}\n")

            logging.info("Security report created")

        except PermissionError:
            logging.error("Cannot write security report")

    def generate_error_log(self):
        report_path = os.path.join(log_dir, "error_log.txt")
        try:
            with open(report_path, "w") as file:
                file.write("=" * 60 + "\n")
                file.write("ERROR LOG\n")
                file.write("=" * 60 + "\n\n")

                file.write(f"Total Errors: {len(self.errors)}\n\n")

                for error in self.errors:
                    file.write(
                        f"[{error['timestamp']}] {error['ip']} - "
                        f"{error['method']} {error['url']} - "
                        f"Status {error['status']}\n"
                    )

            logging.info("Error log created")

        except PermissionError:
            logging.error("Cannot write error log")


def main():
    analyzer = LogAnalyzer(log_file_path)

    try:
        analyzer.process_logs()
        analyzer.generate_summary_report()
        analyzer.generate_security_report()
        analyzer.generate_error_log()

        print("\nAnalysis Complete!")
        print("Total requests:", analyzer.total_requests)
        print("Security incidents:", len(analyzer.security_incidents))
        print("Errors found:", len(analyzer.errors))

        print(f"\nReports generated in '{log_dir}' folder:")
        print("- summary_report.txt")
        print("- security_incidents.txt")
        print("- error_log.txt")
        print("- analysis_audit.log")

    except Exception as error:
        logging.critical(f"Analysis failed: {error}")
        print("Analysis failed:", error)


if __name__ == "__main__":
    main()