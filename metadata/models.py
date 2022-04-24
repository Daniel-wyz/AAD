from django.db import models
from profiles.models import Profile
from django.shortcuts import reverse


## all files uploaded by users
## support: .xlsx
class RawData(models.Model):
    file_name = models.CharField(max_length=120, null=True)
    file_obj = models.FileField(upload_to="rawdata", null=True)

    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file_name


## State for the Record
## Completed
## In work
## Planned
class ProgressState(models.Model):
    state = models.CharField(
        max_length=120,
    )

    def __str__(self):
        return self.state


## Science Keyword with 5 levels
## topic>term>variable1>variable2>variable3
class ScienceKeyword(models.Model):
    topic = models.CharField(max_length=120)
    term = models.CharField(max_length=120, null=True, blank=True)
    variable1 = models.CharField(max_length=120, null=True, blank=True)
    variable2 = models.CharField(max_length=120, null=True, blank=True)
    variable3 = models.CharField(max_length=120, null=True, blank=True)

    full_name = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        ordering = ("full_name",)

    def generate_full_name(self):
        str = f"{self.topic}"
        if self.term:
            str += f" > {self.term}"
        if self.variable1:
            str += f" > {self.variable1}"
        if self.variable2:
            str += f"> {self.variable2}"
        if self.variable3:
            str += f" > {self.variable3}"
        return str

    def __str__(self):
        return self.full_name


## the label that can be analyzed to related ScienceKeyword
class Label(models.Model):
    name = models.CharField(max_length=120, unique=True)
    keywords = models.ManyToManyField(ScienceKeyword)

    def __str__(self):
        return f"{self.name}"


## all metadata information
class Metadata(models.Model):
    ##Internal Information
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    ## General Infomation
    metadata_id = models.CharField(max_length=12, unique=True)
    metadata_name = models.CharField(
        max_length=120,
        null=True,
    )
    aas_project_number = models.CharField(max_length=12, null=True, blank=True)
    parent_metadata_id = models.CharField(max_length=12, null=True, blank=True)
    rawdata = models.ManyToManyField(RawData)
    dataset_progress = models.ForeignKey(
        ProgressState, on_delete=models.PROTECT, null=True
    )

    ##Science Keywords
    science_keywords = models.ManyToManyField(ScienceKeyword)
    additional_keywords = models.TextField(null=True, blank=True)
    instrument = models.CharField(max_length=120, null=True, blank=True)
    platform = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    ##Summary
    summary = models.TextField(default="...", null=True, blank=True)
    purpose = models.TextField(default="...", null=True, blank=True)
    quality = models.TextField(default="...", null=True, blank=True)

    ##Constraints
    use_constraints = models.TextField(default="...", null=True, blank=True)
    access_constraints = models.TextField(default="...", null=True, blank=True)

    ##Publicatiins/References
    references = models.TextField(null=True, blank=True)

    ##Personnel
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    class Meta:
        ordering = ("-time_created",)

    def get_absolute_url(self):
        return reverse("metadata:detail", kwargs={"metadata_id": self.metadata_id})

    def get_pdf_url(self):
        return reverse("metadata:pdf", kwargs={"metadata_id": self.metadata_id})

    def get_xml_url(self):
        return reverse("metadata:xml", kwargs={"metadata_id": self.metadata_id})

    def __str__(self):
        return f"{self.metadata_id}"
