def printAll():
    file = open("Homework folder/mp3Playlist/MyPlaylist.txt", "r")
    for line in file:
        line = line.strip("\n")
        line = line.split(";")
        print(f"Song: {line[0]}, Artist: {line[1]}, Duration: {line[2]}.")
    file.close()


def addSong(songname, songartist, songduration):
    try:
        file = open("Homework folder/mp3Playlist/MyPlaylist.txt", "a")
        line = "\n"+str(songname)+";"+str(songartist)+";"+str(songduration)+";"
        file.write(line)
        file.close()
        print("Song successfully added...")
    except:
        print("An error has occured, try again")
    

def insertSong(songname, songartist, songduration, position):
    try:
        songlist = []
        file = open("Homework folder/mp3Playlist/MyPlaylist.txt", "r")
        for line in file:
            line = line.strip("\n")
            line = line.split(";")
            songlist.append(line)
        file.close()
        count = 0
        wanted_pos = int(position) -1
        after_length = len(songlist)+1
        file = open("Homework folder/mp3Playlist/MyPlaylist.txt", "w")
        while count <= after_length - 1:
            if count < wanted_pos:
                line_format = songlist[count][0]+";"+songlist[count][1]+";"+songlist[count][2]+";\n"
                file.write(line_format)
                count += 1
            elif count == wanted_pos:
                line_format = str(songname)+";"+str(songartist)+";"+str(songduration)+";\n"
                file.write(line_format)
                count += 1
            elif count > wanted_pos:
                line_format = songlist[count-1][0]+";"+songlist[count-1][1]+";"+songlist[count-1][2]+";\n"
                file.write(line_format)
                count += 1
            
    except:
        print("An error has occurred, please try again.")


if __name__ == "__main__":
    insertSong("Happy", "Pharrell Williams", "3:52", 3)
    printAll()

