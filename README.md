## google-drive-backup
This script copies the contents of a specified directory into a specified folder in Google Drive. If you tend to regularly back up files onto your desktop copy of Google Drive, this script is intended for you (although there certainly are easier ways to accomplish the mindless task of periodically backing up files).

## Requirements
This script was tested only on Python 2.7 running on a Windows machine. Also, you need to have Google Drive for Desktop installed and running on your machine.

## Usage
Before you start running the script the first time, please make sure that you complete the following steps:

1. Open the `settings.py` and specify the directories to be backed up. Look for the `SRC` variable. The `SRC` variable is a list which contains one or more 3-tuples. Each 3-tuple, in turn, contains some specifications about the directory to be backed up (see under settins below).
2. Indicate the full path to the Google Drive directory (or a directory inside the Google Drive directory) where you'd like the backed up directories to reside.
3. Save changes to `settings.py` and close the file.
4. Run the script by entering the following on the command line (be sure you're currently in the root directory of this project.):

```
$ python gdrive-copier.py
```

## Settings
To add a directory to be backed up into your Google Drive folder, you need to enter a 3-tuple `(full_path, mode, ignore)` in the `SRC` list variable. The values of this 3-tuple are:

* `full_path`: String representing the full path to the directory you want to back up.
* `mode`: String indicating the mode of copying, either 'tree' or 'dir'. 'tree' mode copies everything in that directory including files and folders in its subdirectories (if any), while 'dir' mode copies only the files in the root level of the specified `full_path` directory.
* `ignore`: A list of strings representing the folder names or filenames in `full_path` to exclude from being copied. If you don't want to ignore any file or folder in `full_path`, just key in an empty list.

By default, there are three 3-tuples provided as part of the `SRC` list. Uncomment or add as many 3-tuples as you need.

## License
[MIT License](https://opensource.org/licenses/MIT)

## Resources
The `copytree` implementation used in this script is largely based on [this Stack Overflow thread]("F:\Projects\google-drive-copier").

## Contributing
Please feel free to make any contribution in any capacity to this project.