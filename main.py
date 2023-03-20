import cv2

# 영상 소스 열기
src = cv2.imread('c:/photo/picture88.jpg')


## 영상처리/컴퓨터 비전 알고리즘 적용##
dst1 = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
dst2 = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
dst3 = src.copy()
_, dst3 = cv2.threshold(dst3, 127, 255, cv2.THRESH_BINARY)







#영상 디스플레이
cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)


# 마무리

cv2.waitKey(0)
cv2.destroyAllWindows()
