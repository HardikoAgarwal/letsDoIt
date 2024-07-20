from django.shortcuts import render

# Create your views here.
def base(request):
    str = 'This is a string'
    number = 16
    data = {
        'string' : str,
        'number' : number,
         
    }
    return render(request,'cool/base.html', data)

def swag(request):
    return render(request, 'cool/swag.html')

def swag_me(request):
    return render(request, 'cool/swag_me.html')

def swag_me_and_you(request):
    return render(request, 'cool/swag_me_and_you.html')