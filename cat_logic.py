import json
from datetime import datetime, date, timedelta

def get_cat_info():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def calculate_age(birth_date, today):
    age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age_months = 12 + today.month - birth_date.month
    else:
        age_months = today.month - birth_date.month
    if today.day >= birth_date.day:
        age_days = today.day - birth_date.day
    else:
        age_months -= 1
        last_month_end = today.replace(day=1) - timedelta(days=1)
        age_days = last_month_end.day - birth_date.day + today.day
    if age_months < 0:
        age_months += 12
    return age_years, age_months, age_days

def generate_message():
    config = get_cat_info()
    cat_name = config["cat_name"]
    birth_date = datetime.strptime(config["birth_date"], "%Y-%m-%d").date()
    known_date = datetime.strptime(config["known_date"], "%Y-%m-%d").date()
    today = date.today()
    known_days = (today - known_date).days + 1
    age_y, age_m, age_d = calculate_age(birth_date, today)
    this_year_birthday = date(today.year, birth_date.month, birth_date.day)
    next_birthday = this_year_birthday if today <= this_year_birthday else date(today.year + 1, birth_date.month, birth_date.day)
    days_to_birthday = (next_birthday - today).days
    message_parts = []
    if days_to_birthday == 0:
        message_parts.append(f"🎉🎂 HAPPY BIRTHDAY {cat_name}！ 🎂🎉")
        message_parts.append(f"今天小壽星 {age_y} 歲了！快給他一個罐罐！")
    elif 0 < days_to_birthday <= 7:
        message_parts.append(f"✨ 距離 {cat_name} 的生日只剩下 {days_to_birthday} 天！✨")
        message_parts.append("生日月慶祝活動開跑囉！")
    message_parts.append(f"今天是你認識 {cat_name} 的第 {known_days} 天")
    message_parts.append(f"{cat_name} 今天 {age_y} 歲 {age_m} 個月又 {age_d} 天大囉")
    if days_to_birthday > 0:
        message_parts.append(f"距離 {cat_name} 的 {age_y+1} 歲生日還有 {days_to_birthday} 天")
    return "\n".join(message_parts)
