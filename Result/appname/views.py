from django.shortcuts import render
from django.http import HttpResponse
from .forms import MarksForm

def calculate_result(request):
    if request.method == 'POST':
        form = MarksForm(request.POST)
        if form.is_valid():
            marks = form.cleaned_data
            division_value = int(request.POST.get('division_value'))  # Get division value from POST data
            total_marks = sum(marks.values())
            pass_status = all(mark >= 35 for mark in marks.values())
            failed_subjects = [subject for subject, mark in marks.items() if mark < 35]
            average_marks = total_marks / division_value
            context = {
                'marks': marks,
                'total_marks': total_marks,
                'pass_status': pass_status,
                'failed_subjects': failed_subjects,
                'average_marks': average_marks,
            }
            return render(request, 'result.html', context)
    else:
        form = MarksForm()
    return render(request, 'calculate.html', {'form': form})
