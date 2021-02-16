from django.db import models

from edc_base.sites import SiteModelMixin
from edc_base.model_mixins import BaseUuidModel

from .performance_assessment import PerformanceAssessment


class PerformanceAssessmentItem(SiteModelMixin, BaseUuidModel):

    performance_assessment = models.ForeignKey(
        PerformanceAssessment,
        on_delete=models.PROTECT)

    kpa_nd_objective = models.CharField(
        verbose_name='KEY PERFORMANCE AREA and OBJECTIVES',
        max_length=250, )

    performance_indicators = models.CharField(
        verbose_name='Key PERFORMANCE INDICATORS / MEASURES & DEADLINES '
                     '(completion dates)',
        max_length=150,)

    weighting = models.CharField(
        verbose_name='%WEIGHTING (KPA Weighting as % of total)',
        max_length=50,)

    mid_year_performance = models.CharField(
        verbose_name='Mid-Year ASSESSMENT (on Performance Results achieved)',
        max_length=100,
        blank=True,
        null=True)

    kpa_rating = models.CharField(
        verbose_name='KPA RATING (Use Rating Scale)',
        max_length=50)

    kpa_score = models.CharField(
        verbose_name='KPA SCORE (Rating x Weighting)',
        max_length=50)

    year_end_assessment = models.CharField(
        verbose_name='Year- End or End of Contract  ASSESSMENT (on Performance'
                     ' Results achieved) Please circle relevant period',
        max_length=100,
        blank=True,
        null=True)

    class Meta:
        verbose_name = 'PERFORMANCE PLANNING & ASSESSMENT'
        verbose_name_plural = 'PERFORMANCE PLANNING & ASSESSMENT'
