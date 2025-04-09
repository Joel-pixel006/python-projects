import qrcode



myqr = qrcode.make("https://www.linkedin.com/feed/?trk=guest_homepage-basic_nav-header-signin")
#converting it into image using pillow
myqr.save("myqr.png", scale = 7)