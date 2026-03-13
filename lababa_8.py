import cv2

# Задание 1:
# img = cv2.imread('variant-10.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
# cv2.imshow('img', thresh)


#Задание 2:
# def video_processing():
#     cap = cv2.VideoCapture(0)
#     down_points = (640, 480)
#     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

        
#         frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         gray = cv2.GaussianBlur(gray, (21, 21), 0)
#         ret, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

#         contours, hierarchy = cv2.findContours(thresh,
#                             cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#         if len(contours) > 0:
#             c = max(contours, key=cv2.contourArea)
#             x, y, w, h = cv2.boundingRect(c)
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#             cv2.putText(frame, f'{x+w//2}:{x+h//2}', (10, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255))
#             cv2.rectangle(frame, (width//2 - 75, height//2 - 75), (width//2 + 75, height//2 + 75), (255, 0, 0), 1)

#             if (width//2 - 75 < x+w//2 < width//2 + 75) and (height//2 - 75 < x+h//2 < height//2 + 75):
#                 frame = cv2.flip(frame, 0)

#         cv2.imshow('frame', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break


# video_processing()
cv2.waitKey(0)
cv2.destroyAllWindows()