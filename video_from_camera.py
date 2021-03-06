import cv2 as cv

def main():
	print(cv.__version__)
	cap = cv.VideoCapture(0)

	while(True):
		ret, frame = cap.read()
		gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

		#Display the resulting frame
		cv.imshow('frame', gray)
		if cv.waitKey(1) & 0xFF == ord('q'):
			break
	#When everything done, release the capture
	cap.release()
	cv.destroyAllWindows()
	
if __name__ == '__main__':
	main()
