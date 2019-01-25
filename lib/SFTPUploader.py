import paramiko


class SFTPUploader:
    """Class for uploading new file to server via SFTP connection."""

    def __init__(self, host: str, port: int, username: str, password: str):
        # connect to server
        transport = paramiko.Transport((host, port))
        transport.connect(
            username=username,
            password=password,
        )
        self._sftp_client = paramiko.SFTPClient.from_transport(transport)

    def save(self, path: str, data: bytes):
        with self._sftp_client.open(path, "wb") as f:
            f.write(data)
