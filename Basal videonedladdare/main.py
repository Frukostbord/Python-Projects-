from pytube import YouTube
import os

# Function for getting URL
def url():

    answer = ""
    # Tries to open URL
    while answer.upper() != "Y":
        link = input("Please paste the URL:\n")
        try:
            yt = YouTube(link)

            v_data = {
                "Title:": yt.title,
                "Views:": yt.views,
                "Published:": yt.publish_date,
                "Length:": f"{yt.length} seconds",
                "Size:": f"{yt.__sizeof__()} mb"
            }

            for i, k in v_data.items():
                print(i, k)
            answer = input("\nIs this input correct?:\nY/N\n")
            if answer.upper() == "Y":
                return yt

        except Exception:
            print("Something went wrong")
            pass


# Pathway to download. Downloads highest quality.
def download(link):

    highest_res_stream = link.streams.get_highest_resolution().itag
    dl = link.streams.get_by_itag(highest_res_stream)
    path = input("Please enter the pathway you want to download the file to.\n")
    path.replace(os.sep,"/")
    file_name = input("Please enter the filename.\n") + ".mp4"


    print("Download starts...")
    try:
        dl.download(output_path=path, filename=file_name)
        print("Download finished!\n")
    except Exception:
        print("Something went wrong. Please look over your pathway and file name.\n")

if __name__ == '__main__':
    while True:
        print("Hello and welcome to the Youtube downloader.")
        selection = input("Select '0' to download a Youtube video.\n"
              "Select '1' to exit\n")

        if selection == "1":
            print("Thank you. Have a great day!")
            break

        elif selection == "0":
            url_check = url()
            if url_check:
                download(url_check)

            print("Download is complete!!")

        else:
            print("Wrong input. Please try again!\n\n")
            continue