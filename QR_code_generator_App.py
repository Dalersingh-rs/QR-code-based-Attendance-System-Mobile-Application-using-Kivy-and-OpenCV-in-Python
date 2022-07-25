from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
# from kivy.core.window import Window
import qrcode
import plyer  # comment this line when converting to apk for android

#uncomment the below code when converting to apk for android
# from jnius import autoclass
# Environment=autoclass('android.os.Environment')
# path=Environment.getExternalStorageDirectory().getAbsolutePath()

# from android.permissions import request_permissions,Permission


class Function(ScreenManager):
    def generate_qr_code(self,root):
        if self.ids.link_text_first.text!='' and self.ids.link_text_last.text!='' and self.ids.link_number.text!='':
            code= qrcode.QRCode(version=1.0,box_size=15,border=4)
            code.add_data(f"{self.ids.link_text_first.text} {self.ids.link_text_last.text}")
            code.make(fit=True)
            img=code.make_image(fill='Black', back_color= 'White')
            img.save(f"{self.ids.link_text_first.text[0]}{self.ids.link_text_last.text[0]}_{self.ids.link_number.text}.png")

            # use the below line when converting the python file to apk for android
            # img.save(f"{path}/{self.ids.link_text_first.text[0]}{self.ids.link_text_last.text[0]}_{self.ids.link_number.text}.png")


            #comment the below code when converting to apk because plyer module throws error in android
            # error is attribute not found attribute.icon()...to rectify error, we should use attribute.presplash()
            plyer.notification.notify(
                title='QR Code Generator',
                message='QR Code Generated'
            )
            self.ids.img_created.source = f"{self.ids.link_text_first.text[0]}{self.ids.link_text_last.text[0]}_{self.ids.link_number.text}.png"
            # self.ids.img_created.source = f"{path}/{self.ids.link_text_first.text[0]}{self.ids.link_text_last.text[0]}_{self.ids.link_number.text}.png"
            root.current = 'image'

        else:
            plyer.notification.notify(
                title='QR Code Generator',
                message='Please type something in the Text Fields'
            )

    def generate_new(self,root):
        self.ids.link_text_first.text=''
        self.ids.link_text_last.text=''
        self.ids.link_number.text=''
        root.current='Welcome_screen'

    def Back(self,root):
        root.current='Welcome_screen'


class Main(MDApp):
    Builder.load_file('layout.kv')
    def build(self):
        return Function()

    # below code used to give permmissions when converting to apk in android
    # def on_start(self):
    #     request_permissions([Permission.READ_EXTERNAL_STORAGE,Permission.WRITE_EXTERNAL_STORAGE])

if __name__ == '__main__':
    Main().run()
