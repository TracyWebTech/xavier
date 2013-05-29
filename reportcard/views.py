
from django.utils.translation import ugettext_lazy as _
from django.views import generic

from accounts.models import Student
from classes.models import Class
#from periods.models import Period


#def get_student_score(student, classroom, subject):#, subperiod):
#    classsub = ClassSubject.objects.get(classroom.classroom, subject=subject)
#    crit = EvaluationCriteria.objects.get(class_subject=classsub)
#    Score(

def get_report_card(student, classroom):

    report_card = {}
    for classsub in classroom.classsubject_set.all():
        subject = []
        report_card.update({classsub.subject: subject})

        for subperiod in classroom.period.subperiod_set.all():
            subperiod = {
                'name': unicode(subperiod),
                'score': student.get_average(subperiod, classsub),
                'absences': 0,
                'frequency': '100%',
            }
            subject.append(subperiod)

    return report_card


class StudentReportCard(generic.TemplateView):
    template_name = 'reportcard/report-card.html'

    def get_context_data(self, **kwargs):
        context = super(StudentReportCard, self).get_context_data(**kwargs)
        class_slug, student_id = context['view'].args

        classroom = Class.objects.get(slug=class_slug)
        student = Student.objects.get(pk=student_id)

        context.update({
            'report_card': get_report_card(student, classroom),
            'student': student,
            'classroom': classroom,
            'title': _('Report Card'),
            'subtitle': student.get_full_name(),
        })
        return context

student_reportcard = StudentReportCard.as_view()
