import qrcode

#this ststemnts below shows using make class and converting it into png format using pillow package

myqr = qrcode.make("https://www.linkedin.com/public-profile/settings?trk=d_flagship3_profile_self_view_public_profile")
#converting it into image using pillow
myqr.save("myqr.png", scale = 7)
