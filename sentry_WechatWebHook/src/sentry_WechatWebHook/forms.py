# coding: utf-8

from django import forms


class WebHookOptionsForm(forms.Form):
    access_token = forms.CharField(
        max_length=255,
        help_text='Webhook robot access_token'
    )
