import sqlite3

conn = sqlite3.connect("youtube_videos.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    print("\n", "*"*70, sep="")
    for row in cursor.fetchall():
        print(f"{row[0]}. {row[1]}, Duration: {row[2]}")
    print("*"*70)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()

def main():
    while True:
        print("\nYoutube Manager App with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit App")
        choice = input("Enter your choice: ")

        if choice=="1":
            list_videos()
        elif choice=="2":
            name = input("Enter the video name: ")
            time= input("Enter the video time: ")
            add_video(name, time)
        elif choice=="3":
            video_id = input("Enter video ID to update: ")
            name = input("Enter the video name: ")
            time= input("Enter the video time: ")
            update_video(video_id, name, time)
        elif  choice=="4":
            video_id = input("Enter the video ID to delete: ")
            delete_video(video_id)
        elif choice=="5":
            break
        else:
            print("Invalid Choice!!! Please Give The Valid Number...")

    conn.close()

if __name__=="__main__":
    main()