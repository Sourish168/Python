import json

filename = "youtube.txt"

def load_data():
    try:
        with open(filename, "r") as file:
            content = file.read().strip()
            if not content:
                return []
            return json.loads(content)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data_helper(videos):
    with open(filename, "w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n","*"*70, sep="")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video["Name"]}, Duration: {video["Time"]}")
    print("*"*70)

def add_video(videos):
    video_name = input("Enter video name: ")
    video_time = input("Enter video length: ")
    videos.append({"Name": video_name, "Time": video_time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    update_num = int(input("Enter the video number to update: "))
    if 1 <= update_num <= len(videos):
        video_name = input("Enter the new video name: ")
        video_time = input("Enter the new video length: ")
        videos[update_num-1] = {"Name": video_name, "Time": video_time}
        save_data_helper(videos)
    else:
        print("Invalid Index Selected!!!")

def delete_video(videos):
    list_all_videos(videos)
    delete_num = int(input("Enter the video number to delete: "))
    if 1 <= delete_num <= len(videos):
        del videos[delete_num-1]
        save_data_helper(videos)
    else:
        print("Invalid Index Selected!!!")

def main():
    videos = load_data()
    while True:
        print("\nYouTube Manager | Choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the application")

        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid Choice!!! Please Give The Valid Number...")

if __name__ == "__main__":
    main()