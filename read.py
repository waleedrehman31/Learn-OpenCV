import cv2 as cv

# Reading Images

# img = cv.imread('Photos/woman.jpg')

# cv.imshow('woman', img)

# Reading Videos

capture = cv.VideoCapture('Videos/Hair.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):  # if letter 'd' is press break out the loop
        break

capture.release()
cv.destroyAllWindows()
