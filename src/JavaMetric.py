import csv
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class JavaMetric:
    path: Path
    package: str
    java_class: str
    lcsec: int = 0
    nvloc: int = 0

    def to_row(self, with_lcsec=False, with_nvloc=False):
        row = [f"./{self.path.as_posix()}", self.package, self.java_class]
        if with_lcsec:
            row.append(str(self.lcsec))
        if with_nvloc:
            row.append(str(self.nvloc))
        return row

    def print(self, with_lcsec=False, with_nvloc=False):
        print(",".join(self.to_row(with_lcsec=with_lcsec, with_nvloc=with_nvloc)))


def read_java_metric_from_csv(csv_file: Path, with_lcsec=False, with_nvloc=False) -> List[JavaMetric]:
    java_metric_list: List[JavaMetric] = []

    with open(csv_file, 'r') as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            java_metric = JavaMetric(Path(row[0]), row[1], row[2])
            position = 3;
            if with_lcsec:
                java_metric.lcsec = row[position]
                position += 1
            if with_nvloc:
                java_metric.nvloc = row[position]

            java_metric_list.append(java_metric)
    return java_metric_list
