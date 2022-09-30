import cv2

list_of_points = []


# Get the mouse position
def get_point(event, x, y, flags, param):
    global list_of_points
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        cv2.circle(image, (x, y), 3, (0, 0, 255), -1)
        list_of_points.append((x, y))
        cv2.imshow('image', image)


# Create a window
scale = 0.5
cap = cv2.VideoCapture(r"D:\Cam_D35\Final\D3_truoc_final.mp4")
ret, image = cap.read()
image = cv2.resize(image, dsize=None, fx=scale, fy=scale)
# image = cv2.imread('test_TDN.png')
cv2.namedWindow('image')
cv2.setMouseCallback('image', get_point)
cv2.imshow('image', image)
key = cv2.waitKey(0)
if key == ord('q'):
    cv2.destroyAllWindows()
elif key == ord('s'):
    with open('../D3/detect_zone.txt', 'w+') as f:
        for point in list_of_points:
            f.write(str(int(point[0] / scale)) + ' ' + str(int(point[1] / scale)) + '\n')
    cv2.destroyAllWindows()
