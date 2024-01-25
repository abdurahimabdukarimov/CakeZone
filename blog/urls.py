from django.urls import path
from .views import index, contact, about, menu, service, team, testimonial

urlpatterns = [
    path("", index, name="index"),
    path("contact/", contact, name="contact"),
    path("about/", about, name="about"),
    path("menu/", menu, name="menu"),
    path("service/", service, name="service"),
    path("team/", team, name="team"),
    path("testimonial/", testimonial, name="testimonial"),

    ]