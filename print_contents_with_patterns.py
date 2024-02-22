import os
import argparse
import fnmatch


def print_file_content(
    directory, ignore_dirs=None, ignore_patterns=None, require_patterns=None, root_directory=None, decode_errors=None
):
    if root_directory is None:
        root_directory = directory
    if ignore_dirs is None:
        ignore_dirs = []
    if ignore_patterns is None:
        ignore_patterns = []
    if require_patterns is None:
        require_patterns = []
    if decode_errors is None:
        decode_errors = []

    # Always ignore .pyc files and __pycache__ folders
    ignore_patterns.append("*.pyc")
    ignore_dirs.append("__pycache__")

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        relative_item_path = os.path.relpath(item_path, root_directory)

        # Skip ignored directories, including __pycache__
        if (
            any(relative_item_path.startswith(ignore_dir) for ignore_dir in ignore_dirs)
            or os.path.basename(item_path) in ignore_dirs
        ):
            continue

        # Check for ignored patterns, including .pyc files
        if any(fnmatch.fnmatch(relative_item_path, pattern) for pattern in ignore_patterns):
            continue

        if os.path.isfile(item_path):
            # Check for required patterns, if specified
            if require_patterns and not any(
                fnmatch.fnmatch(relative_item_path, pattern) for pattern in require_patterns
            ):
                continue

            try:
                with open(item_path, "r", encoding="utf-8") as file:
                    content = file.read()
                print(f"{relative_item_path}:\n{content}\n{'-' * 20}\n")
            except UnicodeDecodeError:
                decode_errors.append(
                    f"Error: Could not decode {relative_item_path}. The file might not be a text file or might use a different encoding."
                )

        elif os.path.isdir(item_path):
            print_file_content(item_path, ignore_dirs, ignore_patterns, require_patterns, root_directory, decode_errors)

    return decode_errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Print file paths and contents with options to ignore or require specific patterns."
    )
    parser.add_argument("directory", type=str, help="The directory to process.")
    parser.add_argument("--ignore", nargs="*", help="Subdirectories to ignore.", default=[])
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--ignore-patterns", nargs="*", help="Filepath patterns to ignore.", default=[])
    group.add_argument("--require-patterns", nargs="*", help="Filepath patterns to strictly require.", default=[])
    args = parser.parse_args()

    ignore_dirs = [os.path.normpath(os.path.join(args.directory, ignore_dir)) for ignore_dir in args.ignore]

    decode_errors = print_file_content(args.directory, ignore_dirs, args.ignore_patterns, args.require_patterns)

    # Print all accumulated decode errors at the end
    if decode_errors:
        print("\nEncountered decode errors in the following files:")
        for error in decode_errors:
            print(error)
