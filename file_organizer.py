
import os
import shutil

def organize_files(folder_path):

    if not os.path.exists(folder_path):
        print("Folder does not exist!")
        return

    for filename in os.listdir(folder_path):

        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):

            extension = filename.split(".")[-1].lower()

            if "." not in filename:
                folder_name = "Others"
            elif extension in ["jpg", "jpeg", "png", "gif"]:
                folder_name = "Images"
            elif extension == "pdf":
                folder_name = "PDFs"
            elif extension in ["doc", "docx", "txt"]:
                folder_name = "Documents"
            elif extension in ["mp4", "mkv", "avi"]:
                folder_name = "Videos"
            elif extension in ["mp3", "wav"]:
                folder_name = "Audio"
            else:
                folder_name = "Others"

            destination_folder = os.path.join(
                folder_path, folder_name
            )

            os.makedirs(destination_folder, exist_ok=True)

            shutil.move(
                file_path,
                os.path.join(destination_folder, filename)
            )

    print("Files organized successfully!")


if __name__ == "__main__":

    folder_path = input("Enter folder path to organize: ")

    organize_files(folder_path)
