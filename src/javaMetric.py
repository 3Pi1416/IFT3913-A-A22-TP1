from dataclasses import dataclass


@dataclass
class javaMetric:
    path: str
    package: str
    java_class: str
    csec: int = None
    jls: int = None
