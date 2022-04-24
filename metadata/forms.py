from django import forms
from .models import Metadata, RawData, ProgressState, ScienceKeyword


# required -- Boolean that specifies whether the field is required.
#             True by default.
# widget -- A Widget class, or instance of a Widget class, that should
#           be used for this Field when displaying it. Each Field has a
#           default Widget that it'll use if you don't specify this. In
#           most cases, the default widget is TextInput.
# label -- A verbose name for this field, for use in displaying this
#          field in a form. By default, Django will use a "pretty"
#          version of the form field name, if the Field is part of a
#          Form.
# initial -- A value to use in this Field's initial display. This value
#            is *not* used as a fallback if data isn't given.
# help_text -- An optional string to use as "help text" for this Field.
# error_messages -- An optional dictionary to override the default
#                   messages that the field will raise.
# show_hidden_initial -- Boolean that specifies if it is needed to render a
#                        hidden widget with initial value after widget.
# validators -- List of additional validators to use
# localize -- Boolean that specifies if the field should be localized.
# disabled -- Boolean that specifies whether the field is disabled, that
#             is its widget is shown in the form but not editable.
# label_suffix -- Suffix to be added to the label. Overrides
#                 form's label_suffix.


class MetadataForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MetadataForm, self).__init__(*args, **kwargs)

        self.fields["metadata_id"].disabled = True
        self.fields["metadata_id"].label = "Metadata ID"
        self.fields["metadata_id"].widget = forms.TextInput(
            attrs={"class": "form-control", "readonly": "true"}
        )

        self.fields["dataset_progress"].initial = ProgressState.objects.get(
            state="Completed"
        )

        self.fields["rawdata"].disabled = True
        self.fields["rawdata"].widget = forms.CheckboxSelectMultiple(
            attrs={"class": "form-control"}
        )

        # self.fields["science_keywords"].widget = forms.HiddenInput()
        # self.fields["science_keywords"].widget = forms.CheckboxSelectMultiple()

    class Meta:
        model = Metadata
        exclude = ("author", "time_created", "time_updated", "science_keywords")
        # labels={
        #     "metadata_id":"Metadata ID"
        # }
        # widgets = {
        #     "metadata_id": forms.TextInput(
        #         attrs={"class": "form-control", "readonly": "true"}
        #     ),
        #     "rawdata": forms.CheckboxSelectMultiple(),
        #     "dataset_progress": forms.Select(choices=ProgressState.objects.all())
        # }


######################################################################
CHART_CHICES = (
    ("Bar Chart", "Bar Chart"),
    ("Pie Chart", "Pie Chart"),
    ("Line Chart", "Line Chart"),
)

KEY_CHICES = (("", ""),)


class MetadataChartForm(forms.Form):
    chart_type = forms.ChoiceField(choices=CHART_CHICES)
    x_key = forms.ChoiceField(choices=KEY_CHICES)
    y_key = forms.ChoiceField(choices=KEY_CHICES)
