import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# fourcc=cv2.videowrite_fourcc(*XVID)
# out=cv2.videowriter('output.avi',fourcc,20.0,(640,480))
while True:
    ret, frame = cap.read()
    #     time.sleep(0.5)
    #     out.write(frame)
    #     img_gray=cv2.cvtcolor(frame,cv2.COLOUR_BGR2GRAY)
    cv2.imshow("webcam", frame)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

# img=np.zeros((512,512,3))
# cv2.rectangle(img,pt1=(100,100),pt2=(300,300),color=(255,0,0),thickness=3)
# cv2.circle(img,centre=(100,400),radius=50,color=(0,0,255),thickness=-1)
# cv2.line(img,pt1=(0,0),pt2=(512,512),thickness=2,color=(0,255,0))
# cv2.puttext(img,org=(400,400),fontscale=4,color=(0,255,255),thickness=2,linetype=cv2.line_AA,text="hello",fontface=cv2.font_italic)
# flag=False
# ix=-1
# iy=-1
# def draw(event,x,y,flags,params):
#  global flag,ix,iy
#  if event==1:
#      cv2.circle(img,centre=(x,y),radius=50,color=(0,0,255),thickness=-1)
# if event==1:
# flag=True
#  ix=x
# iy=y
# elif event==0:
#  if flag==True:
#  cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,255,255),thickness=-1)
# elif event==0:
#  if flag==True:
# cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,255,255),thickness=-1)

# cv2.namedwindow(winname="window")
# cv2.setmousecallback("window",draw)
# img=cv2.imread("image/image.png")
# while True:
#  cv2.imshow('window',img)
# if cv2.waitkey(1) & OXFF==ord('x'):
#  break
# cv2.destroyallwindows()
# img=cv2.imread("imagees/img.png")
# img_resize=cv2.resize(img,(800,800))
# img_resize=cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))

# print(img)
# imgblue=img[:,:,0]
# imggreen=img[:,:,1]
# imgred=img[:,:,2]
# new_img=np.hstack(imgblue,imgred,imggreen)
# img_gray=cv2.cvtcolor(img,cv2.COLOR_BGR2GRAY)
# img_flip=cv2.flip(img,1)
# 1 is horizontal
# -1 is both
# 0 is vertical
# thickness fill karna hai tho -1
# img_crop=img[100:300,200:500]
# for saving
# cv2.imwrite('img.png',img)
# cv2.imshow("window",new_img)
# cv2.imshow('window',img)
# cv2.waitkey(0)
