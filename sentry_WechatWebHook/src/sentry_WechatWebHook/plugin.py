# coding: utf-8

import json

import requests
from sentry.plugins.bases.notify import NotificationPlugin

import sentry_dingding
from .forms import WebHookOptionsForm

# Webhook_API = "https://oapi.dingtalk.com/robot/send?access_token={token}"


class WebHookPlugin(NotificationPlugin):
    """
    Sentry plugin to send error counts to WebHook.
    """
    author = 'sam'
    author_url = 'https://github.com/chxu1989/sentry_WechatWebHook'
    version = sentry_WechatWebHook.VERSION
    description = 'Send error counts to DingDing.'
    resource_links = [
        ('Source', 'https://github.com/chxu1989/sentry_WechatWebHook'),
        ('Bug Tracker', 'https://github.com/chxu1989/sentry_WechatWebHook/issues'),
        ('README', 'https://github.com/chxu1989/sentry_WechatWebHook/master/README.md'),
    ]

    slug = 'WebHook'
    title = 'WebHook'
    conf_key = slug
    conf_title = title
    project_conf_form = WebHookOptionsForm

    def is_configured(self, project):
        """
        Check if plugin is configured.
        """
        return bool(self.get_option('access_token', project))

    def notify_users(self, group, event, *args, **kwargs):
        self.post_process(group, event, *args, **kwargs)

    def post_process(self, group, event, *args, **kwargs):
        """
        Process error.
        """
        if not self.is_configured(group.project):
            return

        if group.is_ignored():
            return

        # access_token = self.get_option('access_token', group.project)
        send_url = self.get_option('access_token', group.project)
        title = u"New alert from {}".format(event.project.slug)

        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "content": u"#### {title} \n > {message} [href]({url})".format(
                    title=title,
                    message=event.message,
                    url=u"{}events/{}/".format(group.get_absolute_url(), event.id),
                )
            }
        }
        requests.post(
            url=send_url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data).encode("utf-8")
        )
