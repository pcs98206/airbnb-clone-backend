from django.contrib import admin
from .models import Review

# Register your models here.
class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"
    parameter_name = "payload"

    def lookups(self, request, model_admin):
        return [
            ("관리자페이지에 나타날 값1", "관리자페이지에 나타날 값1"),
            ("good", "good"),
            ("깔끔", "깔끔"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            return reviews


class GoodReviewFilter(admin.SimpleListFilter):
    title = "Good or Bad"
    parameter_name = "rating"

    def lookups(self, request, model_admin):
        return [
            ("good review", "Good Review"),
            ("bad review", "Bad Review"),
        ]

    def queryset(self, request, ratings):
        exist = self.value()
        if exist == "good review":
            return ratings.filter(rating__gte=3)
        elif exist == "bad review":
            return ratings.filter(rating__lt=3)
        else:
            return ratings


@admin.register(Review)
class ReivewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        WordFilter,
        GoodReviewFilter,
        "rating",
        "user__is_host",
        "room__category",
    )
