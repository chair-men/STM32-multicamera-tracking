import cv2
import os

image_folders = ['EPFL-RLC_dataset/frames/cam0', 'EPFL-RLC_dataset/frames/cam1', 'EPFL-RLC_dataset/frames/cam2']
video_names = ['sample_video/video_3/cam0.mp4', 'sample_video/video_3/cam1.mp4','sample_video/video_3/cam2.mp4']


if __name__ == "__main__":
    for image_folder, video_name in zip(image_folders, video_names):
        images = [img for img in os.listdir(image_folder) if img.endswith(".jpeg")]
        frame = cv2.imread(os.path.join(image_folder, images[0]))
        height, width, layers = frame.shape

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video = cv2.VideoWriter(video_name, fourcc, 30, (width,height))

        i = 0

        for image in images:
            video.write(cv2.imread(os.path.join(image_folder, image)))
            if i == 600:
                break
            i += 1

        cv2.destroyAllWindows()
        video.release()