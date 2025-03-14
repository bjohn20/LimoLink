from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    pickup_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}), 
        label="Pickup Date & Time"
    )

    class Meta:
        model = Booking
        fields = [
            "client", "driver", "pickup_street_address", "pickup_city", "pickup_state", "pickup_zip_code", "pickup_time",
            "dropoff_street_address", "dropoff_city", "dropoff_state", "dropoff_zip_code", "airline", "other_airline", "passengers", "fare", "payment_method"
        ]
        widgets = {
            "pickup_street_address": forms.TextInput(attrs={"placeholder": "123 Main St"}),
            "pickup_city": forms.TextInput(attrs={"placeholder": "City"}),
            "pickup_state": forms.TextInput(attrs={"value": "GA", "readonly": "readonly"}),
            "pickup_zip_code": forms.TextInput(attrs={"placeholder": "ZIP Code"}),
            "dropoff_street_address": forms.TextInput(attrs={"placeholder": "123 Main St"}),
            "dropoff_city": forms.TextInput(attrs={"placeholder": "City"}),
            "dropoff_state": forms.TextInput(attrs={"value": "GA", "readonly": "readonly"}),
            "dropoff_zip_code": forms.TextInput(attrs={"placeholder": "ZIP Code"}),
        }

    # Custom clean method to validate 'airline' and 'other_airline'
    def clean(self):
        cleaned_data = super().clean()  # Get all cleaned form data
        airline = cleaned_data.get("airline")  # Get the selected airline value
        other_airline = cleaned_data.get("other_airline")  # Get the "Other Airline" value

        # If "Other" is selected for airline but no other airline is specified
        if airline == "Other" and not other_airline:
            self.add_error("other_airline", "Please specify the airline.")  # Add error for 'other_airline'

        return cleaned_data  # Return the cleaned data after validation
