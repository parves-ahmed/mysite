from django.db import models

# Create your models here.


class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_by
    # updated_by

    class Meta:
        abstract = True


class Companies(CommonInfo):
    company_name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.company_name


class Designations(CommonInfo):
    designation_name = models.CharField('designation', max_length=30)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    from_date = models.DateField('from_date')
    to_date = models.DateField('to_date', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.designation_name


class ProjectType(CommonInfo):
    project_type_name = models.CharField('Platform', max_length=15)

    class Meta:
        db_table = 'Project Platform'

    def __str__(self):
        return self.project_type_name


class Languages(CommonInfo):
    language_name = models.CharField(max_length=10)

    def __str__(self):
        return self.language_name


class Databases(CommonInfo):
    database_name = models.CharField(max_length=10)

    def __str__(self):
        return self.database_name


class Frontend(CommonInfo):
    front_end = models.CharField('Frontend', max_length=25)

    def __str__(self):
        return self.front_end


class Backend(CommonInfo):
    backend_name = models.CharField('Backend', max_length=25)

    def __str__(self):
        return self.backend_name


class VersionControls(CommonInfo):
    vct_name = models.CharField('Version Control Tool', max_length=12)

    def __str__(self):
        return self.vct_name


class ReportTools(CommonInfo):
    tool_name = models.CharField('Report Tools', max_length=20)

    def __str__(self):
        return self.tool_name


class Projects(CommonInfo):
    company = models.ForeignKey(Companies, models.CASCADE)
    designation = models.ForeignKey(Designations, models.CASCADE)
    project_name = models.CharField(max_length=30)
    project_type = models.ForeignKey(ProjectType, models.CASCADE, null=True, blank=True)
    language = models.ForeignKey(Languages, models.CASCADE, null=True, blank=True)
    front_end = models.ForeignKey(Frontend, models.CASCADE, null=True, blank=True)
    back_end = models.ForeignKey(Backend, models.CASCADE, null=True, blank=True)
    version_control = models.ForeignKey(VersionControls, models.CASCADE, null=True, blank=True)
    report_tools = models.ForeignKey(ReportTools, models.CASCADE, null=True, blank=True)
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date', null=True, blank=True)

    def __str__(self):
        return self.project_name


class Trainings(CommonInfo):
    training_name = models.CharField(max_length=30)
    org_by = models.CharField('Organised By', max_length=30)
    from_date = models.DateField('From Date')
    to_Date = models.DateField('To Date', null=True, blank=True)
    certificate = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.training_name


class Achievements(CommonInfo):
    event_name = models.CharField(max_length=70)
    event_date = models.DateField('Event Date')
    event_org = models.CharField('Event Organizer', max_length=30)
    certificate = models.ImageField()
    position = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.event_name


class CoverImage(CommonInfo):
    photos = models.ImageField(upload_to='images/')





