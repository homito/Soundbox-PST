import time

metadata = {
    "title": "Seul la musique",
    "artist_name": "Frank",
    "album_name": "La folle aventure de Seul",
    "status": "paused"
}    

with open('metadata.py', 'w') as file:
    with open('output.txt', 'r') as f:
        while True:
            line = f.readline()
            file.writelines(line)
            if not line:
                time.sleep(0.1)
                continue
            print(line + 'written')


with open('output.txt', 'r') as file:
    

# with open("output.txt", "r") as f:
#     metadata["title"] = "dinde"
#     metadata["artist_name"] = "dinde"
#     metadata["album_name"] = "dinde"
#     metadata["status"] = "dinde"

# with open('metadata.txt','w') as file:
#     metadata["title"]
#     print("metadata written")