# Usage Guide for Sple Artifacts Uploader

This guide provides an overview of all the commands available in the Sple Artifacts Uploader application.

## Commands

### 1. `--help`

Displays help information for the application and for specific commands.

**Usage:**

```bash
sple-artifacts-uploader [command] --help
```

### 2. `--version`

Displays the current version of the Sple Artifacts Uploader.

**Usage:**

```bash
sple-artifacts-uploader --version
```

### 3. `upload-file`

Uploads a file to a specified destination URL.

**Usage:**

```bash
sple-artifacts-uploader upload-file --artifact-path <path> --destination-url <url> --username <username> --password <password> [--timeout <seconds>]
```

**Options:**

- `--artifact-path (PATH)`: Path to the file to upload (required).
- `--destination-url (TEXT)`: Destination URL for the upload (required).
- `--username (TEXT)`: Username for authentication (required).
- `--password (TEXT)`: Password for authentication (required).
- `--timeout (INTEGER)`: Timeout for the upload in seconds (optional, default is 10 seconds).
