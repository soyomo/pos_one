from django.shortcuts import render
def pos_list(request):
    return render(request, 'pos/pos_list.html', {})
# Create your views here.
