import cv2

# 영상 소스 열기
src = cv2.imread('c:/photo/picture88.jpg')


## 영상처리/컴퓨터 비전 알고리즘 적용##
dst1 = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
dst2 = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
dst3 = src.copy()
_, dst3 = cv2.threshold(dst3, 127, 255, cv2.THRESH_BINARY)

dst4= cv2.bitwise_not(src)

# 이미지의 모든 행과 열의 절반만 선택
height, width, channel = src.shape
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
dst5 = cv2.warpAffine(src, matrix, (width, height))




#영상 디스플레이
cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imshow('dst4', dst4)
cv2.imshow('dst5', dst5)
# 마무리

cv2.waitKey(0)
cv2.destroyAllWindows()
print("git hub 연동 확인")



