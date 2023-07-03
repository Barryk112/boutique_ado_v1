from django.shortcuts import render

def profile(request):
    """ Display te usrers profile """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
