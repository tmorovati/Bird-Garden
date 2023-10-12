from pydub import AudioSegment
import numpy as np

class add_mth_wave_files: 
    def __init__(self,  file, destination, duration = 0.5 ):
          self.file = file 
          self.destination = destination
          
      
    def add_AudioFile(self , file,   input_directory ):
            # we need to define this global[8]
            global accumulated_audio
        
            if str(file).endswith("wav"):
                  wav_path = input_directory + str(f"/{file}")
                  audio = AudioSegment.from_wav(wav_path)
                  accumulated_audio = accumulated_audio.append(audio , crossfade=0)
                  duration = audio.duration_seconds         
            
            return accumulated_audio, duration
            
    def add_Silence(self, audio, duration):
          # in qesmat ro inja ezafe mikonam vali byd be on for e ezafe koni
          silence_segment = AudioSegment.silent(duration=duration)
          audio = audio + silence_segment
          duration = silence_segment.duration_seconds
          return audio
          
    def add_White_Noise(self, audio, snr_dB):
          
          audio_std = np.std(audio.get_array_of_samples())
          noise_std = audio_std / (10 ** (snr_dB / 20.0))
          noise = np.random.normal(scale=noise_std, size=len(audio))
          noise = AudioSegment(audio.raw._spawn(noise.astype(np.int16)))
          
          # Overlay the white noise onto the audio data
          audio_with_noise = audio.overlay(noise)
          
          return audio_with_noise
          