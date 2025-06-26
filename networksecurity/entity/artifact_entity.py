from dataclasses import dataclass


@dataclass
class DataInputArtifact:
    trained_file_path: str
    test_file_path: str