# -*- coding: utf-8 -*-

import cv2
import numpy as np
from PIL import Image
import pytesseract


# lê e reduz a imagem
img = cv2.pyrDown(cv2.imread('eng.font.exp0.jpg'))

# coloca em gray sclae e threshold (binariza) a imagem
ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                180, 255, cv2.THRESH_BINARY)
# acha os contornos e pega o mais externo
image, contours, hier = cv2.findContours(threshed_img, cv2.RETR_TREE,
                cv2.CHAIN_APPROX_SIMPLE)
                
tesseract eng.font.exp0.jpg eng.font.exp0 batch.nochop makebox
cv2.imshow('image', image)
cv2.waitKey(0)
x = 0
for contour in contours:
    # print(contour)
    # print(counters)
    if cv2.contourArea(contour) < 180:
        continue

    rect = cv2.minAreaRect(contour)
    box = cv2.boxPoints(rect)

    ext_left = tuple(contour[contour[:, :, 0].argmin()][0])
    ext_right = tuple(contour[contour[:, :, 0].argmax()][0])
    ext_top = tuple(contour[contour[:, :, 1].argmin()][0])
    ext_bot = tuple(contour[contour[:, :, 1].argmax()][0])

    roi_corners = np.array([box], dtype=np.int32)

    cv2.polylines(image, roi_corners, 1, (255, 0, 0), 3)
    # draw a green rectangle to visualize the bounding rect
    #     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cropped_image = threshed_img[ext_top[1]:ext_bot[1], ext_left[0]:ext_right[0]]
    # file_nameAux = contour
    y = str(x)
    # cv2.imshow('image', image)
    # cv2.waitKey(0)
    # cv2.imwrite('crop'+y+'.jpg', cropped_image)
    x = x + 1
    print (x)

# # with each contour, draw boundingRect in green
# # a minAreaRect in red and
# # a minEnclosingCircle in blue
# for c in contours:
#     # get the bounding rect
#     x, y, w, h = cv2.boundingRect(c)
#     # draw a green rectangle to visualize the bounding rect
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
#
#     # get the min area rect
#     rect = cv2.minAreaRect(c)
#     box = cv2.boxPoints(rect)
#     # convert all coordinates floating point values to int
#     box = np.int0(box)
#     # draw a red 'nghien' rectangle
#     cv2.drawContours(img, [box], 0, (0, 0, 255))

    # # finally, get the min enclosing circle
    # (x, y), radius = cv2.minEnclosingCircle(c)
    # # convert all values to int
    # center = (int(x), int(y))
    # radius = int(radius)
    # # and draw the circle in blue
    # img = cv2.circle(img, center, radius, (255, 0, 0), 2)

# print(len(contours))
# cv2.drawContours(img, contours, -1, (255, 255, 0), 1)

##################################################################
# cropped, x, y = [], [], []
#
# for contour_line in contours:
#     for contour in contour_line:
#         x.append(contour[0][0])
#         y.append(contour[0][1])
#
# x1, x2, y1, y2 = min(x), max(x), min(y), max(y)
#
# for i in range(1, 160):
#     cropped = img[y1:y2, x1:x2]
#     cv2.imshow("cropped", cropped[i])

################################################################

# cropped, x, y = [], [], []
#
# for contour_line in contours:
#     for contour in contour_line:
#         x.append(contour[0][0])
#         y.append(contour[0][1])

# for cont in x:
#     cropped.(img[y[cont]:y[cont+1], x[cont]:x[cont+1]])

#int i = 0;

#while( i < y.length){
#    cropped.append(img[y[cont]:y[cont+1], x[cont]:x[cont+1]])
#    i = i + 2;
#}
#for(i = 0; i < copped.length; i++){
#    cv2.imshow("cropped", cropped[i])
#}
########################################################################
# for contour in contours:
#
#     if cv2.contourArea(contour) < 200:
#         continue
#
#     rect = cv2.minAreaRect(contour)
#     box = cv2.boxPoints(rect)
#
#     ext_left = tuple(contour[contour[:, :, 0].argmin()][0])
#     ext_right = tuple(contour[contour[:, :, 0].argmax()][0])
#     ext_top = tuple(contour[contour[:, :, 1].argmin()][0])
#     ext_bot = tuple(contour[contour[:, :, 1].argmax()][0])
#
#     roi_corners = np.array([box], dtype=np.int32)
#
#     cv2.polylines(bounding_box_image, roi_corners, 1, (255, 0, 0), 3)
#     cv2.imshow('image', bounding_box_image)
#     cv2.waitKey(0)
#
#     cropped_image = grayimage[ext_top[1]:ext_bot[1], ext_left[0]:ext_right[0]]
#     cv2.imwrite('crop.jpg', cropped_image)

# cv2.imshow("contours", img)
# text = pytesseract.image_to_string(img)  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
# print(text)

ESC = 27
cv2.waitKey(0)
cv2.destroyAllWindows()
