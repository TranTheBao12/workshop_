import os
import re
from datetime import datetime

# Thư mục gốc chứa nội dung Hugo
content_dir = r"C:\Users\USER\Desktop\PromoVideoGenerator_aws\000000-Workshop\000058-SessionManager\000058-SessionManager\content"

# Các định dạng ngày hợp lệ (có thể mở rộng thêm nếu cần)
valid_date_formats = ["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"]

def is_valid_date(date_str):
    for fmt in valid_date_formats:
        try:
            datetime.strptime(date_str, fmt)
            return True
        except ValueError:
            continue
    return False

def fix_date_line(line):
    # Dò tìm dòng date (dùng cho cả TOML và YAML)
    match = re.match(r'(date\s*[=:]\s*)(["\']?)(.+?)\2\s*$', line)
    if match:
        prefix, quote, date_str = match.groups()
        if not is_valid_date(date_str):
            # Nếu date không hợp lệ, thay bằng ngày hôm nay
            fixed_date = datetime.today().strftime('%Y-%m-%d')
            return f'{prefix}"{fixed_date}"\n'
    return line

def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    in_front_matter = False
    delimiter = None
    modified = False
    new_lines = []

    for line in lines:
        # Phát hiện bắt đầu hoặc kết thúc front matter
        if line.strip() in ["+++", "---"]:
            if not in_front_matter:
                delimiter = line.strip()
                in_front_matter = True
            else:
                in_front_matter = False
            new_lines.append(line)
            continue

        if in_front_matter:
            fixed_line = fix_date_line(line)
            if fixed_line != line:
                modified = True
            new_lines.append(fixed_line)
        else:
            new_lines.append(line)

    if modified:
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print(f"✔ Đã sửa: {file_path}")

def walk_and_fix_dates():
    for root, _, files in os.walk(content_dir):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                process_file(full_path)

if __name__ == "__main__":
    walk_and_fix_dates()
