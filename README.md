# Password Manager

A simple command-line password manager written in Python that allows users to securely store, retrieve, and manage their credentials.
A lot more changes incoming (I'm still working on this one..contributions are welcome!)

## Features
- Securely add new credentials (service, username, password)
- Retrieve stored credentials
- Password-protected access
- Automatic data deletion after multiple failed attempts
- Uses CSV file for storage

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required dependencies (install via `pip install -r requirements.txt` if needed)

## Installation
1. Clone the repository:
   ```sh
   git clone git@github.com:kish-0/psswdmgn.git
   cd psswdmgn
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Running the Script
The script can be run from outside the project root using:
```sh
python3 -m psswdmgn -n <service_name>
```

### Adding a New Password
To add a new password:
```sh
python3 -m psswdmgn [-n/--newpsswd] <service_name>
```
- Failure to provide `<service_name>` will result in a `ValueError`.
- You will be prompted to enter a username and password.

### Viewing Passwords
- To view password of specific `<service_name>`:
   ```sh
   python3 -m psswdmgn [-v/--view] <service_name>
   ```
   - `<service_name>` is optional in this case.
   - You will be prompted for a username if viewing a specific service.

- To view all stored credentials:
   ```sh
   python3 -m psswdmgn [-v/--view]
   ```

### Deleting Passwords
To delete a stored password:
```sh
python3 -m psswdmgn [-d/--delete] <service_name>
```
- Failure to provide `<service_name>` will result in a `ValueError`.
- You will be prompted to enter a username and password.

### Security Password
On running the script, you will be asked to enter a security password. Failing three attempts will delete all stored data.

## Notes
- Ensure you remember your security password.
- Be cautious as failing to enter the correct security password three times will erase all stored data.
- Default security password is 'hi'

## Future
- The security password is just stored in plain sight in the scripts code, which will be changed in the future.
- Encryption might be added.
## License
This project is licensed under the MIT License.

