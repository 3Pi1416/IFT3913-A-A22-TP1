import csv
from dataclasses import dataclass
from typing import List
from pathlib import Path


@dataclass
class JavaMetric:
    # jls: int = None
    path: Path
    package: str
    java_class: str

    def print(self):
        print(f"./{self.path.as_posix()},{self.package},{self.java_class}")


def read_java_metric_from_csv(csv_file: Path) -> List[JavaMetric]:
    java_metric_list: List[JavaMetric] = []

    with open(csv_file, 'r') as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            java_metric = JavaMetric(Path(row[0]), row[1], row[2])
            java_metric_list.append(java_metric)
    return java_metric_list


@dataclass
class JavaMetricLcsec(JavaMetric):
    lcsec: int = 0

    def print(self):
        print(f"./{self.path},{self.package},{self.java_class},{self.lcsec}")


def read_java_metric_lcsec_from_csv(csv_file: Path) -> List[JavaMetricLcsec]:
    java_metric_list: List[JavaMetricLcsec] = []

    with open(csv_file, 'r') as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            java_metric = JavaMetricLcsec(Path(row[0]), row[1], row[2], int(row[3]))
            java_metric_list.append(java_metric)
    return java_metric_list
