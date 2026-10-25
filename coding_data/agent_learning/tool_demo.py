import os,json

def write_note(filename,content):
    with open(filename,'w',encoding="utf_8" )as f:
        f.write(content)
    
    if __name__ == "__main__":
        write_note("my_note.txt","what will we learn today?")
        print("success")