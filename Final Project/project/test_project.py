import os
import tempfile
from project import scan_folder, compare_folders, generate_report

def test_scan_folder():
    # Create a temporary directory with one file
    with tempfile.TemporaryDirectory() as tmp:
        file_path = os.path.join(tmp, "example.txt")
        with open(file_path, "w") as f:
            f.write("hello")

        result = scan_folder(tmp)

        # The file should appear in the results
        assert "example.txt" in result
        # The timestamp should be a float
        assert isinstance(result["example.txt"], float)

def test_compare_folders():
    source = {"a.txt": 200.0, "b.txt": 300.0}
    backup = {"a.txt": 100.0, "b.txt": 300.0}

    result = compare_folders(source, backup)

    # a.txt is outdated because backup timestamp < source timestamp
    assert "a.txt" in result["outdated"]
    # b.txt matches exactly
    assert "b.txt" in result["matched"]
    # No missing files in this scenario
    assert result["missing"] == []

def test_generate_report():
    results = {
        "missing": ["x.txt"],
        "outdated": ["y.txt"],
        "matched": ["z.txt"]
    }

    report = generate_report(results)

    # Check that each section appears in the report
    assert "Missing files:" in report
    assert "- x.txt" in report

    assert "Outdated files:" in report
    assert "- y.txt" in report

    assert "Matched files:" in report
    assert "- z.txt" in report
