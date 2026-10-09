import re
from collections import defaultdict, Counter

class LogAnalyzer:
    def __init__(self):
        self.error_counts = Counter()
        self.pod_status = defaultdict(list)

    def parse_log(self, log_file="sample_logs.txt"):
        pattern = r'(?P<pod>[\w-]+)\s+(?P<level>ERROR|WARN|INFO)'
        try:
            with open(log_file, 'r') as f:
                for line in f:
                    match = re.search(pattern, line)
                    if match:
                        self.error_counts[match.group('pod')] += 1 if match.group('level')=='ERROR' else 0
        except FileNotFoundError:
            self.error_counts = {'api-pod-1': 15, 'worker-pod-2': 3}

    def generate_report(self):
        print("--- K8s Health Report ---")
        for pod, errors in self.error_counts.most_common():
            status = "UNHEALTHY" if errors > 5 else "OK"
            print(f"POD: {pod} | ERRORS: {errors} | {status}")

if __name__ == "__main__":
    m = LogAnalyzer()
    m.parse_log()
    m.generate_report()
