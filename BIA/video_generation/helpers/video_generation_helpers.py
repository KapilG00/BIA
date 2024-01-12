from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip


class VideoGenerationHelper:
    def __init__(self):
        pass

    def generate_sample_video(self):
        success = False
        try:
            # Load the input video clip
            video_clip = VideoFileClip('media/sample_video.mp4')

            # Add a text overlay to the video
            text_clip = TextClip("Niagara Falls!!", font="Amiri-bold", fontsize=80, color='black')
            text_clip = text_clip.set_position('center').set_duration(video_clip.duration)

            # Composite the video clip and text clip
            final_clip = CompositeVideoClip([video_clip, text_clip])

            # Output video file path
            output_video_path = 'media/output_video.mp4'

            # Write the result to a file
            final_clip.write_videofile(output_video_path, codec='libx264', audio_codec='aac')
            success = True
        except OSError as err:
            raise Exception(f"Error in file operation: {err}")    
        except Exception as e:
            raise Exception(str(e))
        finally:
            video_clip.close()
            text_clip.close()
            final_clip.close()

        return success
     

