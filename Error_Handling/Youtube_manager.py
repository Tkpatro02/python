
def list_all_videos():
    pass
def add_video():
    pass
def update_video():
    pass
def Delete_videos():
    pass
def load_data():
    pass

def main():
    videos=load_data()
    while True:
        print("\n Youtube Manager | choose an option")

        print("1. List all Youtube videos")
        print("2.Add a youtube video")
        print("3.Update a Youtube video details")
        print("4.Delete a Youtube video")
        print("5.Exit the app")

        choice=input("Enter Correct Choice")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                Delete_videos(videos)
            case '5':
                break
            case _:
                print("invalid choice")

if __name__=="__main__":
    main()
