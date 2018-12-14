from dropbox import *
from tkinter import *
from tkinter import filedialog
from os.path import *
from itertools import *

acccountToken = Dropbox("INSERT_YOUR_ACCESSTOKEN_IN_HERE")

print("You have connected to this account:", acccountToken.users_get_current_account())


def upload():
    root.fName = filedialog.askopenfilename(initialdir = ".",\
                                            title = "Select a file you want to upload",\
                                            filetypes = (('text files','*.txt'),("all files","*.*")))
    def fileName(aString):
        lastSolidusLocation = aString.rfind("/")
        fName = aString[lastSolidusLocation+1:]
        return fName
    fName = fileName(root.fName)
    DropboxLocation = "/NewFolder/"

    with open(root.fName,'rb') as file:
        uploading = acccountToken.files_upload(file.read(), DropboxLocation+fName, mode=dropbox.files.WriteMode("overwrite"))

        shareLinkCreated = acccountToken.sharing_create_shared_link(DropboxLocation+fName)

        print("\nThis is the link to access your files: " + shareLinkCreated.url)
root = Tk()
root.title("Dropbox Uploader"); root.minsize(300,100)
root.config()
button = Button(root,text="Chosing File",command =upload)
button.pack()
root.mainloop()
