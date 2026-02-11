import os

def scan_folder(path):
    """
    Scan a folder and return a dictionary mapping filenames
    to their last modified timestamps.

    Args:
        path (str): Path to the folder.

    Returns:
        dict: {filename: timestamp}
    """
    files = {}

    if not os.path.isdir(path):
        return files

    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        if os.path.isfile(full_path):
            files[item] = os.path.getmtime(full_path)

    return files

def compare_folders(source_files, backup_files):
    """
    Compare source and backup file dictionaries and determine
    which files are missing, outdated, or matched.

    Args:
        source_files (dict): Files from the source folder.
        backup_files (dict): Files from the backup folder.

    Returns:
        dict: {
            "missing": [...],
            "outdated": [...],
            "matched": [...]
        }
    """
    results = {
        "missing": [],
        "outdated": [],
        "matched": []
    }

    for filename, src_time in source_files.items():
        if filename not in backup_files:
            results["missing"].append(filename)
        else:
            backup_time = backup_files[filename]
            if backup_time < src_time:
                results["outdated"].append(filename)
            else:
                results["matched"].append(filename)

    return results

def generate_report(results):
    """
    Generate a human-readable report summarizing the backup status.

    Args:
        results (dict): Output from compare_folders.

    Returns:
        str: Formatted report.
    """
    lines = []

    lines.append("Missing files:")
    if results["missing"]:
        for filename in results["missing"]:
            lines.append(f"- {filename}")
    else:
        lines.append("None")

    lines.append("\nOutdated files:")
    if results["outdated"]:
        for filename in results["outdated"]:
            lines.append(f"- {filename}")
    else:
        lines.append("None")

    lines.append("\nMatched files:")
    if results["matched"]:
        for filename in results["matched"]:
            lines.append(f"- {filename}")
    else:
        lines.append("None")

    if results["missing"] or results["outdated"]:
        lines.append("\nBackup is incomplete.")
    else:
        lines.append("\nBackup is complete.")

    return "\n".join(lines)

def main():
    """
    Main program flow:
    - Ask user for source and backup paths
    - Scan both folders
    - Compare results
    - Print report
    """
    source = input("Enter source folder path: ").strip()
    backup = input("Enter backup folder path: ").strip()

    print("\nChecking backup...\n")

    source_files = scan_folder(source)
    backup_files = scan_folder(backup)

    results = compare_folders(source_files, backup_files)
    report = generate_report(results)

    print(report)

if __name__ == "__main__":
    main()
