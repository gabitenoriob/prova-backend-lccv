from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"
    
class PaginaInicial(TemplateView):
    template_name = "admin/index.html"


