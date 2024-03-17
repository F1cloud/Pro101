import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for fileName in files:
                localPath = os.path.join(root, fileName)
                relativePath = os.path.relpath(localPath, file_from)
                dropboxPath = os.path.join(file_to, relativePath)

        with open(localPath, 'rb') as f:
            dbx.files_upload(f.read(), dropboxPath, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BtLAg1t-1FPzsddQGwd08VTl0HtBUhxw59C4WXWJlRc1lTBdTtK1QHGf4Qtz-SUpXKTke33PAntVZUFeog1hJdcGBLkTm1HBXkPF9MkTLjNC1mtfiev3qUov_GD89qcy4gEHbP7KNnNv'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()
