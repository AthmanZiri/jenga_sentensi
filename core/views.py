from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Record


def record(request):
    if request.method == "POST":
        audio_file = request.FILES.get("recorded_audio")
        use_case_audio_file = request.FILES.get("recorded_use_case")
        word = request.POST.get("word")
        language = request.POST.get("language")
        # meaning = request.POST.get("meaning")
        meaning_in_english = request.POST.get("meaning_in_english")
        meaning_in_swahili = request.POST.get("meaning_in_swahili")
        record = Record.objects.create(
            language=language, voice_record=audio_file, 
            voice_record_use_case=use_case_audio_file,
            word=word, meaning_in_english=meaning_in_english, meaning_in_swahili=meaning_in_swahili)
        record.save()
        messages.success(request, "Audio recording successfully added!")
        return JsonResponse(
            {
                "url": record.get_absolute_url(),
                "success": True,
            }
        )
    context = {"page_title": "Record audio"}
    return render(request, "core/record.html", context)


def record_detail(request, id):
    record = get_object_or_404(Record, id=id)
    context = {
        "page_title": "Recorded audio detail",
        "record": record,
    }
    return render(request, "core/record_detail.html", context)


def index(request):
    records = Record.objects.all()
    context = {"page_title": "Voice records", "records": records}
    return render(request, "core/index.html", context)
