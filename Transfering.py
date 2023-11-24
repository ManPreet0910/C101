import dropbox

class TransferData:
    def __init__(self, acess_token):
        self.acess_token = acess_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.acess_token)
        f = open(file_from, 'rb') 
        dbx.files_upload(f.read(), file_to)

def main():
    acess_token = "sl.BqeQKKOB1qzWhWrDEhTAhGGGLEfVwJedCWSsnyJNr_T31yK1LC82E3VDMR_1q6uV2XJlTqb_k4N5rp0Iu7S7zwRqseU8edgxJ59F3eMuAT_5GjdAHIivnZskKqncuAE9wyOc0R2NrAVY"
    
    transferdata = TransferData(acess_token)
    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to uplaod to DropBox: ")
   
    transferdata.uplaod_file(file_from, file_to)

main()
