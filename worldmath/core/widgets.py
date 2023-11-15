from django.forms import RadioSelect


class GovbrSelect(RadioSelect):
    template_name = "widgets/naoseipqum.html"
    option_template_name = "widgets/naoseipqdois.html"