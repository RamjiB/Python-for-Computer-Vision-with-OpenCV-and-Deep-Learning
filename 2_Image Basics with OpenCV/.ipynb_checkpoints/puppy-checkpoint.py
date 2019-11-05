import cv2
img = cv2.imread('../Data/00-puppy.jpg')

while True:
    cv2.imshow('Puppy',img)
    # if we have waited for 1 ms AND we have pressed the Esc key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
