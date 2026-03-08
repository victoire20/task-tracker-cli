from datetime import datetime


def format_datetime(dt_str: str | None = None) -> str:
    if  not dt_str:
        return '-'
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S.%f")
    return dt.strftime("%d/%m/%Y %H:%M")