from django.shortcuts import render, redirect
from formapp.models import StudentModel

# Create your views here.
def home_view(request):
    
    s_data = StudentModel.objects.all()
    
    context = {
       'st_data' : s_data 
    }
    
    return render(request, 'home.html', context)


def add_studnt(request):
    
    if request.method == 'POST':
        
        vs_id = request.POST.get('s_id')
        vs_name = request.POST.get('s_name')
        vs_email = request.POST.get('s_email')
        vs_dept = request.POST.get('s_dept')
        vs_address = request.POST.get('s_address')
        
        StudentModel.objects.create(
            st_id = vs_id,
            st_name = vs_name,
            st_email = vs_email,
            st_dept = vs_dept,
            st_address = vs_address
        )
        
        return redirect('home_page') #Redirect Using Name Parameter
    
    return render(request, 'add_student.html')