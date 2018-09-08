from django.shortcuts import render, render_to_response


# Create your views here.
def index(request):
   if request.user.is_authenicated:
       base_template_name = 'admin/base_admin.html'
   else:
       base_template_name = 'admin/base.html'

   # Pass base template name to the renderer
   return render_to_response('admin/base.html', {'base_template_name':base_template_name})
