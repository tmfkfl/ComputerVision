import cv2

# 영상 소스 열기
src = cv2.imread('c:/photo/picture01.jpg')












#영상 디스플레이
cv2.imshow('src', src)




# 마무리

cv2.waitKey(0)
cv2.destroyAllWindows()
