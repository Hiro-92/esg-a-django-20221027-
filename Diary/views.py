from django.shortcuts import render, redirect
from Diary.forms import MemoryForm
from Diary.models import Memory

def memory_list(request):
    # 전체 포스팅을 가져올 준비. 아직 가져오지는 않음.
    diary_qs = Memory.objects.all().order_by("-id")
    return render(request, "Diary/memory_list.html",{
        "memory_list":diary_qs,
    }) # render 함수에 3번째로 딕셔너리 가능

def memory_detail(request, pk):
    post = Memory.objects.get(pk = pk)
    return render(
        request,
        "Diary/memory_detail.html",
        {
            "post":post,
        }
    )
    
def diary_new(request):
    # print("request.method = ", request.method)
    # print("request.POST =", request.POST)
    if request.method == "GET":
        form = MemoryForm()
    else:
        form = MemoryForm(request.POST)
        if form.is_valid():
            # 유효성 검사에 통과한 값들이 저장된 dict
            # form.cleaned_data
            post = form.save() # ModelForm에서 지원
            # return redirect("/blog/")
            # return redirect(f"/blog/{post.pk}")
            # return redirect(post.get_absolute_url())
            return redirect(post)
            
    return render(request, "Diary/memory_new.html", {
        "form":form,
    })