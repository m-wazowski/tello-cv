def video_recorder(pipe_conn, save_video, height=300, width=400):
    global video_writer
    # create a VideoWrite object, recoring to ./video.avi
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    if video_writer is None and save_video == True:
        video_file = f"video_{datetime.now().strftime('%d-%m-%Y_%I-%M-%S_%p')}.mp4"
        video_writer = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*'MP4V'), 30, (width, height))

    while True:
        frame = pipe_conn.recv()
        video_writer.write(frame)
        time.sleep(1 / 30)

    # then we got the exit event so cleanup
    signal_handler(None, None)
