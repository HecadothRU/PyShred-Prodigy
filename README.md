# PyShred Prodigy Data Sanitization Tool

## Overview
This Python script is designed as a basic data sanitization tool for Unix-like systems. Its primary function is to securely erase data from storage devices, making data recovery extremely difficult, if not impossible. This script is a demonstration and educational tool and should be used cautiously.

## Features

### Dynamic Drive Detection
- Lists all writable block devices on Unix-like systems.
- Utilizes the `lsblk` command to identify available drives, excluding read-only devices.

### Data Overwrite Methods
- Offers two methods for data overwriting: `zeros` (overwrites with zero bytes) and `random` (overwrites with pseudo-random bytes).
- The random data overwrite uses a fixed seed for the random number generator, enabling predictable patterns for verification.

### Enhanced Efficiency
- Increased block size to 4MB for faster overwriting, improving performance on large drives.

### Error Handling
- Implements basic error handling for write operations.
- Attempts to continue the sanitization process even when encountering bad sectors or write errors.

### Three-Pass Overwrite
- A simple three-pass overwrite method is used, where each pass writes a different data pattern.
- While not adhering to any specific standard, it resembles some basic methods used in data sanitization.

### Progress Feedback
- Provides real-time progress feedback during both the overwriting and verification phases.
- Displays the percentage of completion for each pass.

### Verification Process
- After overwriting, the script attempts to verify that the data has been securely erased.
- Reads back the data to ensure it matches the expected overwrite pattern.

## Limitations and Considerations

- **Risk of Data Loss**: Directly writes to disk drives, which can result in irreversible data loss if used improperly.
- **No SSD Optimization**: Does not account for complexities of SSDs, such as wear-leveling algorithms.
- **Platform-Specific**: Tailored for Unix-like systems and may require adjustments for other operating systems.
- **Not Standards Compliant**: Does not explicitly comply with professional data sanitization standards like NIST 800-88 or DoD 5220.22-M.
- **Limited Error Handling**: Basic error handling is implemented, but more robust handling and logging would be advisable for professional tools.
- **User Caution**: Requires careful selection of the target drive to avoid accidental data loss.

## Conclusion

This script serves as a basic example of how data sanitization can be approached using Python. It demonstrates key concepts but is not a substitute for professionally developed and certified data sanitization tools, especially in environments where data security and compliance with specific standards are critical.

## Usage Instructions

1. **List Drives**: Run the script to list all available drives.
2. **Select Drive**: Enter the drive path you wish to sanitize (e.g., `/dev/sda`).
3. **Choose Method**: Select the sanitization method - `zeros` for zero-fill, `random` for random data fill.
4. **Start Sanitization**: The script will start the sanitization process and display progress.
5. **Verification**: After overwriting, the script will verify the sanitization.

**Warning**: This tool will irreversibly erase data on the selected drive. Use with extreme caution.
