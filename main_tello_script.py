
if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    run_pid = True
    track_face = True  # True - cause the Tello to start to track/follow a face
    save_video = True
    fly = True

    parent_conn, child_conn = Pipe()
    parent2_conn, child2_conn = Pipe()

    exit_event = Event()

    with Manager() as manager:
        p1 = Process(target=track_face_in_video_feed,
                     args=(exit_event, child_conn, child2_conn, run_pid, track_face, fly,))
        p2 = Process(target=show_video, args=(exit_event, parent_conn,))
        p3 = Process(target=video_recorder, args=(parent2_conn, save_video,))
        p2.start()
        p3.start()
        p1.start()

        p1.join()
        p2.terminate()
        p3.terminate()
        p2.join()
        p3.join()

    print("Complete...")
