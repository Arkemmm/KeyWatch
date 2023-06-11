# KeyWatch

KeyWatch is a keylogger written in Python.

## Table of Contents

- [KeyWatch](#keywatch)
- [Description](#description)
- [List of Features](#list-of-features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Contributing](#contributing)

## Description

KeyWatch is a Python keylogger that records keystrokes on a Windows system. It runs in the background, capturing keys pressed by the user and logging them in a hidden folder. Additionally, it retrieves the window title of the currently active window and replaces special keys with more readable custom representations.

## List of Features

- **Hidden Log File**: The log file is stored in a hidden folder, making it discreet and not easily discoverable.
- **Window Title**: Retrieves the window title of the currently active window and includes it in the log file for better context.
- **Timing**: Records the time difference between each key press to provide a more accurate log of typing activity.
- **Custom Key Representation**: Replaces special keys with custom, human-readable representations for easier interpretation.
- **Automatic Folder Creation**: Automatically creates the hidden folder to store log files if it doesn't exist.
- **Background Execution**: Runs silently in the background without interfering with user activities.
- **Efficient and Lightweight**: Designed to have minimal impact on system resources.

## Getting Started

To get started with KeyWatch, follow these steps:

1. Clone the repository or download the ZIP file.
2. Install the required dependencies.

## Usage

To use KeyWatch, follow the steps below:

1. Run the Python script `keywatch.py` using the command `python keywatch.py`.
2. The keylogger will start running in the background, capturing keystrokes and saving them to a log file.
3. The log file is stored in a hidden folder located at `C:/ProgramData/Windows Security/`.
4. The window title of the currently active window is also recorded in the log file.

Example usage:

```bash
python keywatch.py
```

## Dependencies

KeyWatch requires the following Python libraries:

- keyboard
- pywin32

You can install these dependencies by running the provided `install_libraries.bat` file.

## Installation

To install KeyWatch, follow these steps:

1. Clone the repository or download the ZIP file.
2. Run the `install_libraries.bat` file to install the required Python libraries.

## Configuration

There is no additional configuration required for KeyWatch. However, you can modify the `KEY_MAP` dictionary in the `keywatch.py` file to customize the representation of special keys.

## Contributing

Contributions to KeyWatch are welcome! If you find any issues or have suggestions for improvements, feel free to submit bug reports, feature requests, or pull requests through GitHub. You can get in touch with the development team by contacting @Arkemmm.
