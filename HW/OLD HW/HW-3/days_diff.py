from datetime import datetime
def days_diff(start_date: str, end_date: str) -> int:
    """
    calculate number of days between two dates.
    найти разницу между двумя датами
    """
    sdt = datetime.strptime(start_date, "%d-%m-%Y")
    edt = datetime.strptime(end_date, "%d-%m-%Y")
    return (edt - sdt).days

sdt = '01-02-2009'
edt = '01-01-2010'
print('09 Days:', days_diff(sdt, edt))