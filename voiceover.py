from dotenv import load_dotenv
import sys
import os
from elevenlabs.client import ElevenLabs

print(os.getcwd())

load_dotenv()

_api_key=os.getenv("ELEVEN_LABS_KEY")
_voice_id=os.getenv("VOICE_ID")

if not _api_key:
    print("No api-key found: api-key needed for voiceover")
    sys.exit()
if not _voice_id:
    print("voice id needed for voiceover, found None")
    sys.exit()
    
_ec=ElevenLabs(api_key=_api_key)

def create_voice_file(txt:str,file_name:str):
    audio_byts=_ec.text_to_speech.convert(
        text=txt,
        voice_id=_voice_id,
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128")
    
    with open(file_name+".mp3","wb") as f:        
        for b in audio_byts:
            f.write(b) 
        
      
   