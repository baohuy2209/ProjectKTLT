from pathlib import Path

# Đường dẫn tới file
file_path = Path("tests\\test_read_file\\folder1") / "text.txt"

with file_path.open("r", encoding="utf-8") as file:
    content = file.read()
    print(content)
