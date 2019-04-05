from django.db import models
from django.utils.html import escape
from django.utils.safestring import mark_safe


class Gamer(models.Model):
    tag = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=True, default="Bob")
    email_address = models.EmailField()
    steam_id = models.CharField(max_length=200, blank=True, default="NA")
    ps_network_id = models.CharField(max_length=200, blank=True, default="NA")
    xbox_id = models.CharField(max_length=200, blank=True, default="NA")

    def __str__(self):
        return self.tag


class SelfEvaluation(models.Model):
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    q1 = models.CharField(max_length=1)
    q2 = models.CharField(max_length=1)
    q3 = models.CharField(max_length=1)
    q4 = models.CharField(max_length=1)
    q5 = models.CharField(max_length=1)
    q6 = models.CharField(max_length=1)
    q7 = models.CharField(max_length=1)
    q8 = models.CharField(max_length=1)
    q9 = models.CharField(max_length=1)
    q10 = models.CharField(max_length=1)
    q11 = models.CharField(max_length=1)
    q12 = models.CharField(max_length=1)

    def __str__(self):
        return str(self.gamer.name)
        # return str(self.gamer.name) + ' q1:' + str(self.q1) + ' q2:' + str(self.q2) + ' q3:' + str(
        #     self.q3) + ' q4' + str(self.q4) + ' q5:' + str(self.q5) + ' q6:' + str(self.q6) + ' q7:' + str(
        #     self.q7) + ' q8:' + str(self.q8) + ' q9:' + str(self.q9) + ' q10:' + str(self.q10) + ' q11:' + str(
        #     self.q11) + ' q12:' + str(self.q12)


class PreferenceEvaluation(models.Model):
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    q1 = models.CharField(max_length=1)
    q2 = models.CharField(max_length=1)
    q3 = models.CharField(max_length=1)
    q4 = models.CharField(max_length=1)
    q5 = models.CharField(max_length=1)
    q6 = models.CharField(max_length=1)
    q7 = models.CharField(max_length=1)
    q8 = models.CharField(max_length=1)
    q9 = models.CharField(max_length=1)
    q10 = models.CharField(max_length=1)
    q11 = models.CharField(max_length=1)
    q12 = models.CharField(max_length=1)

    def __str__(self):
        return str(self.gamer.name)
        # return str(self.gamer.name) + ' q1:' + str(self.q1) + ' q2:' + str(self.q2) + ' q3:' + str(
        #     self.q3) + ' q4' + str(self.q4) + ' q5:' + str(self.q5) + ' q6:' + str(self.q6) + ' q7:' + str(
        #     self.q7) + ' q8:' + str(self.q8) + ' q9:' + str(self.q9) + ' q10:' + str(self.q10) + ' q11:' + str(
        #     self.q11) + ' q12:' + str(self.q12)
