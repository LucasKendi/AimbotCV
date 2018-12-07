import cv2
import numpy as np
import mss

with mss.mss() as sct:
	monitor = {"top": 95, "left": 65, "width": 550, "height": 400}
	while "Screen capturing":
		img = np.array(sct.grab(monitor))

		cv2.imshow('img', img)
		if cv2.waitKey(25) & 0xFF == ord("q"):
			cv2.destroyAllWindows()
			break