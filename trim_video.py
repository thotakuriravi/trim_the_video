from moviepy.editor import VideoFileClip
import os

# Path to the folder containing the videos
folder_path = "happy_and_healthy\\multil\\english\\intro\\"

# Maximum duration in seconds
max_duration = 5

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".mp4") or filename.endswith(".avi"):
        video_path = os.path.join(folder_path, filename)
        
        # Load the video clip
        video = VideoFileClip(video_path)
        
        # Check if video duration is greater than max_duration
        if video.duration > max_duration:
            # Set the duration of the video to max_duration
            video = video.set_duration(max_duration)
            
        # Export the video with the same filename
        new_path = folder_path+'new\\'
        os.makedirs(new_path, exist_ok= True)
        # If we want here we can also mention the new file_name instead of old_name
        modified_video_path = os.path.join(new_path, filename)
        video.write_videofile(modified_video_path)
        
        # Close the video clip
        video.close()
