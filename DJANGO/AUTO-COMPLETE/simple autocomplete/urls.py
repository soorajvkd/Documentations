urlpatterns = [
    ...
    url(r'^doctor-autocomplete/$',DoctorsAutocomplete.as_view(),name='doctor_autocomplete'),
    ...
]
