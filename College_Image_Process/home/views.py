from django.shortcuts import render
from .models import ImageUpload


def index(request):
	img=ImageUpload.objects.all()
	p=img[len(img)-1].image
	print(p.url)
	content ={'image': p.url}
	return render(request,"home/index.html", content)

def uploadImage(request):
	riverImage=request.FILES['image-river']
	image=ImageUpload(image=riverImage)
	image.save()
	
	return render(request,"home/index.html")
	