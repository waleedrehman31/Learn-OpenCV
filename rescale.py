import cv2 as cv

# Reading Images

img = cv.imread('Photos/woman.jpg')
cv.imshow('woman', img)

# rescale Function


def rescaleFrame(frame, scale=0.75):
    # this is working for video, images and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[1] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Rescaling image
rezied_image = rescaleFrame(img, scale=.2)
# output rescaling image
cv.imshow('Rezied imaged', rezied_image)

# rescaling video function


def changeRes(width, height):
    # this is only work for live video
    capture.set(3, width)
    capture.set(4, height)


# --------- Reading Videos ---------------
capture = cv.VideoCapture('Videos/Hair.mp4')

while True:
    isTrue, frame = capture.read()

# Rescalling Video
    frame_resize = rescaleFrame(frame, scale=.2)

# Showing Videos
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resize)

    if cv.waitKey(20) & 0xFF == ord('d'):  # if letter 'd' is press break out the loop
        break

capture.release()
cv.destroyAllWindows()
