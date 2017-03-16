from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
#imported os to change directory
import os

#from uploads.core.models import Document
#from uploads.core.forms import DocumentForm


#def home(request):
#     documents = Document.objects.all()
#     return render(request, 'core/home.html', { 'documents': documents })

def home(request):
    return render(request, 'core/home.html')
    
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        import separateLeadStereoParam
        new_name = 'media/' + filename
        separateLeadStereoParam.main(new_name)
        os.chdir('media/karaoke/')
        os.rename('estimated_music_VUIMM.wav',filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url , 'filename' : filename
        })

    return render(request, 'core/simple_upload.html')


# def model_form_upload(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = DocumentForm()
#     return render(request, 'core/model_form_upload.html', {
#         'form': form
#     })
