import cv2 as cv

def main():
	#cv.NameWindow("VideoExample", cv.WINDOW_AUTOSIZE)
	cap = cv.VideoCapture('meeting.mp4')

	while(cap.isOpened()):
		ret, frame = cap.read()
		gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
		cv.imshow('frame', gray)

		if cv.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release
	cv.destroyAllWindows()


if __name__ == '__main__':
	main()