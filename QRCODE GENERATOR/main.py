import qrcode
#pip install qrcode and pip install Pillow
class Myqr:
    def __init__(self, size: int, padding :int):
        self.qr=qrcode.QRCode(box_size=size,border=padding)

    def create_qr(self, file_name: str , fg: str, bg: str):
        user_input: str=input("ENTER TEXT: ")

        try:
            self.qr.add_data(user_input)
            qr_image=self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)

            print(f"SUCCESSFULLY CREATED ({file_name})")
        except Exception as e:
            print(f"ERROR {e}")



def main():
    myqr=Myqr(size=30,padding=2)
    myqr.create_qr('sample.png',
                   fg="green",
                   bg="white")
    

    
if __name__ =="__main__":
    main()
