def show_video(exit_event, pipe_conn):
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    while True:
        frame = pipe_conn.recv()
        # display the frame to the screen
        cv2.imshow("Drone Face Tracking", frame)
        cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            exit_event.set()
