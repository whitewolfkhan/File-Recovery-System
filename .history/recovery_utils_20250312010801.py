import os

# Define file signatures for multiple file types.
FILE_SIGNATURES = {
    "jpg": ("jpg", b"\xff\xd8\xff", b"\xff\xd9"),
    "png": ("png", b"\x89PNG\r\n\x1a\n", b"IEND\xaeB`\x82"),
    "pdf": ("pdf", b"%PDF", b"%%EOF"),
    # Add more file types as needed.
}

def recover_by_signature(disk_path, output_dir, chunk_size=4096):
    """
    Scans the raw partition (disk_path) for deleted files using file carving.
    It looks for known file headers and footers (from FILE_SIGNATURES) in a sliding buffer.
    Carved files are saved in output_dir.
    Returns a list of recovered file paths.
    """
    os.makedirs(output_dir, exist_ok=True)
    recovered_files = []
    file_index = 1

    with open(disk_path, "rb") as disk:
        buffer = b"" #byte string data store
        while True:
            chunk = disk.read(chunk_size)
            if not chunk:
                break
            buffer += chunk

            for key, (extension, header, footer) in FILE_SIGNATURES.items():
                start = buffer.find(header)
                while start != -1:
                    end = buffer.find(footer, start)
                    if end != -1:
                        end += len(footer)
                        file_data = buffer[start:end]
                        filename = os.path.join(output_dir, f"carved_{file_index}.{extension}")
                        try:
                            with open(filename, "wb") as f:
                                f.write(file_data)
                            recovered_files.append(filename)
                            print(f"Recovered file: {filename}")
                        except Exception as e:
                            print(f"Error writing {filename}: {e}")
                        file_index += 1
                        buffer = buffer[end:]
                        start = buffer.find(header)
                    else:
                        # Footer not found; keep unprocessed part
                        buffer = buffer[start:]
                        break
            # Prevent buffer from growing indefinitely
            if len(buffer) > chunk_size * 10:
                buffer = buffer[-chunk_size * 10:]
    return recovered_files

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



