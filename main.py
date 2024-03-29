import cv2
import numpy as np

#funcao para evitar paradas por erro
def nothing(x):
    pass

#execução da camera
cap= cv2.VideoCapture(0)

#Criação da janela
cv2.namedWindow('trackbars')

#criar trackbars

cv2.createTrackbar('l-h','trackbars',0,179,nothing)
cv2.createTrackbar('l-s','trackbars',0,255,nothing)
cv2.createTrackbar('l-v','trackbars',0,255,nothing)
cv2.createTrackbar('u-h','trackbars',255,255,nothing)
cv2.createTrackbar('u-s','trackbars',255,255,nothing)
cv2.createTrackbar('u-v','trackbars',255,255,nothing)


#loop

while(True):
    #leitura do frame
    ret,frame=cap.read()
    #pega os valores da trackbar
    l_h=cv2.getTrackbarPos('l-h','trackbars')
    l_s=cv2.getTrackbarPos('l-s','trackbars')
    l_v=cv2.getTrackbarPos('l-v','trackbars')
    u_h=cv2.getTrackbarPos('u-h','trackbars')
    u_s=cv2.getTrackbarPos('u-s','trackbars')
    u_v=cv2.getTrackbarPos('u-v','trackbars')
    
    #array numpy Lowe upper
    lower=np.array([l_h,l_v,l_v])
    upper=np.array([u_h,u_v,u_v])
    
    #criar o hsv
    hsv=cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)
    
    #criar Mascara
    
    mask=cv2.inRange(hsv,lower,upper)
    
    #exibir frame original
    cv2.imshow('frame',frame)
    
    #exibir mask
    cv2.imshow('frame',mask)
    
    #waitkey
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
    
    #finalização
    cap.release()
    #cv2.destroyAllWindows()
    
    
    

