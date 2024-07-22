import cv2

src = cv2.imread("tuffpic.png", cv2.IMREAD_UNCHANGED)

#og image = 577x432

scale = int(input("What percent scale would you like?"))

nwid = int(src.shape[1] * scale / 100)
nlen = int(src.shape[0] * scale / 100)


dimensions = (nwid, nlen)

output = cv2.resize(src, dimensions)
cv2.imwrite("newImage.png", output)
cv2.waitKey(0)