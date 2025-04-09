import qrcode



myqr = qrcode.make("https://www.linkedin.com/public-profile/settings?trk=d_flagship3_profile_self_view_public_profile")
#converting it into image using pillow
myqr.save("myqr.png", scale = 7)