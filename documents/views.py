from django.shortcuts import render
from django.http import FileResponse
from .forms import SpecForm
from core.utils.pdf_utils import generate_spec_pdf

def generate_spec_view(request):
    if request.method == 'POST':
        form = SpecForm(request.POST)
        if form.is_valid():
            pdf_file = generate_spec_pdf(form.cleaned_data)
            return FileResponse(pdf_file, as_attachment=True)
    else:
        form = SpecForm()
    return render(request, 'documents/spec_form.html', {'form': form})


from .forms import COAForm
from core.utils.pdf_utils import generate_coa_pdf

def generate_coa_view(request):
    if request.method == 'POST':
        form = COAForm(request.POST)
        if form.is_valid():
            pdf_file = generate_coa_pdf(form.cleaned_data)
            return FileResponse(pdf_file, as_attachment=True)
    else:
        form = COAForm()
    return render(request, 'documents/coa_form.html', {'form': form})


from .forms import MSDSForm
from core.utils.pdf_utils import generate_msds_pdf

def generate_msds_view(request):
    if request.method == 'POST':
        form = MSDSForm(request.POST)
        if form.is_valid():
            pdf_file = generate_msds_pdf(form.cleaned_data)
            return FileResponse(pdf_file, as_attachment=True)
    else:
        form = MSDSForm()
    return render(request, 'documents/msds_form.html', {'form': form})


from .forms import MSDSForm
from core.utils.pdf_utils import generate_msds_pdf

def generate_msds_view(request):
    if request.method == 'POST':
        form = MSDSForm(request.POST)
        if form.is_valid():
            pdf_file = generate_msds_pdf(form.cleaned_data)
            return FileResponse(pdf_file, as_attachment=True)
    else:
        form = MSDSForm()
    return render(request, 'documents/msds_form.html', {'form': form})


from .forms import SelectCodeForm
from core.utils.db_utils import calculate_weighted_parameters
from data_management.models import Main, Spec
from core.utils.pdf_utils import generate_spec_pdf
from django.http import FileResponse
import datetime

def select_spec_view(request):
    if request.method == 'POST':
        form = SelectCodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            main = Main.objects.get(code=code)
            spec = Spec.objects.get(productcode=code)
            weights = calculate_weighted_parameters(code)

            data = {
                "tscode": code,
                "productname": main.name,
                "date": datetime.date.today(),
                "color": spec.color,
                "specific_gravity": weights['sg_range'],
                "refractive_index": weights['ri_range'],
                "flash_point": weights['flash_point'],
                "shelf_life": spec.exp,
                "supersede": "—"
            }

            pdf_file = generate_spec_pdf(data)
            return FileResponse(pdf_file, as_attachment=True)
    else:
        form = SelectCodeForm()

    return render(request, 'documents/select_spec_form.html', {'form': form})
