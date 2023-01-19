"""Google AnalyticsトラッキングID設定ファイル"""
from django.conf import settings


def get_ga_tracking_id(request):
    """
    Google Analytics トラッキングIDを返す
    DEBUG=Falseの場合にのみ有効

    Parameters
    ----------
    request: django.core.handlers.wsgi.WSGIRequest
        リクエストオブジェクト

    Returns
    -------
    GOOGLE_ANALYTICS_TRACKING_ID: dict
        Google AnalyticsトラッキングID
    """
    ga_tracking_id = getattr(settings, 'GOOGLE_ANALYTICS_TRACKING_ID', False)
    if not settings.DEBUG and ga_tracking_id:
        return {
            'GOOGLE_ANALYTICS_TRACKING_ID': ga_tracking_id,
        }
    return {}
