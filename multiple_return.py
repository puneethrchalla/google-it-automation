def organize_time(seconds):
    hours = seconds // 3600
    minutes = (seconds - (hours * 3600)) // 60
    seconds = seconds - (hours * 3600) - (minutes * 60)
    return hours, minutes, seconds

print(organize_time(65))