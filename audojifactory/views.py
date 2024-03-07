from django.http import JsonResponse
from django.views import View
from audojifactory.creator import AudojiCreator

class TranscribeView(View):
    async def post(self, request, *args, **kwargs):
        # Assuming the audio_file_url is sent in the body of the POST request
        data = await request.json()
        audio_file_url = data.get('audio_file_url')
        
        if not audio_file_url:
            return JsonResponse({'error': 'audio_file_url is required'}, status=400)

        creator = AudojiCreator(audio_file_url)
        try:
            transcription_result = await creator.transcribe_audio()
            return JsonResponse(transcription_result, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)