import csv
from datetime import datetime
import os
from typing import List

# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http import HttpResponse


class MakeUserReportService:
    def _extract_username_list(self) -> List[str]:
        User = get_user_model()
        return User.objects.all()
        # return list(User.objects.values_list("username", flat=True))

    def _generate_file_name(self) -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        return "{}_{}".format("user_report", timestamp)

    def _load_username_list_to_csv(
        self, file_name: str, username_list: List[str]
    ) -> str:
        full_path = f"reports/{file_name}.csv"

        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["username", "password"])
            writer.writerows(
                ([username, username.password] for username in username_list)
            )

        return full_path

    def execute(self) -> str:
        username_list = self._extract_username_list()
        file_name = self._generate_file_name()

        return HttpResponse(self._load_username_list_to_csv(file_name, username_list))


# =================================================================

# Чтение CSV-файла
# with open("data.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# Запись в CSV-файл
# with open("data.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Имя", "Фамилия", "Возраст"])
#     writer.writerow(["Иван", "Иванов", "30"])
#     writer.writerow(["Анна", "Петрова", "25"])

# =================================================================
