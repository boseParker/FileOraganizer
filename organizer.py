import os
import shutil
import logging

# Setup logging
logging.basicConfig(
    filename='file_organizer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# File extension mapping
EXTENSION_MAP = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c"]
}

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def get_category(extension):
    for category, extensions in EXTENSION_MAP.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_files(target_folder):
    if not os.path.isdir(target_folder):
        print("Invalid directory path!")
        return

    try:
        for filename in os.listdir(target_folder):
            file_path = os.path.join(target_folder, filename)

            if os.path.isfile(file_path):
                _, extension = os.path.splitext(filename)
                category = get_category(extension)

                destination_folder = os.path.join(target_folder, category)
                create_folder_if_not_exists(destination_folder)

                destination_path = os.path.join(destination_folder, filename)

                shutil.move(file_path, destination_path)
                logging.info(f"Moved: {filename} → {category}/")

        print("Files organized successfully!")
        logging.info("File organization completed.")

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        print(f"Error occurred: {str(e)}")

# ---- Run Script ----
if __name__ == "__main__":
    path = input("Enter the full path of the folder to organize: ").strip()
    organize_files(path)


