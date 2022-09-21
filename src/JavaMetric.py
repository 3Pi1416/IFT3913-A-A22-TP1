from dataclasses import dataclass


@dataclass
class JavaMetric:
    # csec: int = None
    # jls: int = None
    path: str
    package: str
    java_class: str

    def print(self):
        print(f"{self.path},{self.package},{self.java_class}")
