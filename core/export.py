import csv
import json
from pathlib import Path
from datetime import datetime

from config import EXPORT_DIR


class SessionExporter:
    #Класс экспорта истории Pomodoro-сессий.
    
    def __init__(self):
        #Создание экспортера.
        
        self.export_dir = Path(
            EXPORT_DIR
        )

        self.export_dir.mkdir(
            exist_ok=True
        )


    # Экспорт в CSV
    
    def export_csv(
            self,
            sessions,
            filename=None
    ):
        #Экспортирует сессии в CSV-файл.

        if filename is None:

            filename = (
                f"pomodoro_export_"
                f"{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                ".csv"
            )


        filepath = (
            self.export_dir /
            filename
        )


        if not sessions:
            return None


        fields = [
            "id",
            "date",
            "start_time",
            "end_time",
            "duration",
            "session_type",
            "completed",
            "weekday"
        ]


        with open(
            filepath,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=fields
            )


            writer.writeheader()


            for session in sessions:

                writer.writerow(
                    {
                        field:
                            session.get(field, "")
                        for field in fields
                    }
                )


        return filepath



    # Экспорт в JSON
    
    def export_json(
            self,
            sessions,
            filename=None
    ):
        #Экспортирует историю в JSON.

        if filename is None:

            filename = (
                f"pomodoro_export_"
                f"{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                ".json"
            )


        filepath = (
            self.export_dir /
            filename
        )


        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as file:


            json.dump(
                sessions,
                file,
                indent=4,
                ensure_ascii=False
            )


        return filepath



    # Экспорт отчета аналитики

    def export_report(
            self,
            report,
            filename=None
    ):
        #Экспортирует аналитический отчет.
        
        if filename is None:

            filename = (
                f"analytics_report_"
                f"{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                ".json"
            )


        filepath = (
            self.export_dir /
            filename
        )


        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as file:


            json.dump(
                report,
                file,
                indent=4,
                ensure_ascii=False
            )


        return filepath
