from datetime import datetime

import pandas as pd
import re
import time

start_time = time.time()


"""
logs = []
with open("../../data/rawData/worker-c660-20_11_2023.log", "r", encoding="utf-8") as file:
    logs = file.readlines()[:150000]
"""




def process_logs(logs):
    start_time = time.time()

    df = pd.DataFrame(columns=['heure', 'niveau', 'tache'])
    line_count = 0

    for log in logs:
        line_count += 1
        max_line_length = 1000
        if len(log) > max_line_length:
            log = log[:max_line_length]
        heure = log[1:24]
        print(line_count)
        tache = ""
        if re.match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}", heure):
            niveau_matches = re.findall(r": (.*?)/", log)
            if len(niveau_matches) > 1:
                niveau_matches = niveau_matches[0]
            niveau_matches = re.search(r"(INFO|ERROR|WARNING)", log)
            niveau = niveau_matches.group(1) if niveau_matches else "N/A"
            tache_matches = re.search(r"Task (\S+)(?=\[)|(\S+)(?=\[)", log)
            if tache_matches:
                tache = tache_matches.group(1) if tache_matches.group(1) else tache_matches.group(2)
            else:
                tache = "System"
            """
            tache_matches = re.findall(r"((\S+)(?=\[)|\s)", log)
            if tache_matches[0][0]:
                tache = tache_matches[0][0] if tache_matches else "N/A"
            else:
                tache = tache_matches[0] if tache_matches else "N/A"

            tache = tache.replace("Received task:", "")
            tache = tache.replace("Task", "")
            tache = tache.replace(" ", "")
            """


            df = df.append({'heure': heure, 'niveau': niveau, 'tache': tache}, ignore_index=True)

    unique_niveaux = df['niveau'].unique()
    print("Différents types de niveau:", unique_niveaux)

    info_counts = df['niveau'].value_counts(normalize=True, dropna=False)
    task_counts = df['tache'].value_counts()
    niveau_counts = df['niveau'].value_counts()

    print(niveau_counts)

    print("-------------------------------------")
    print(df.head())
    print(df.info())
    print(df.describe())
    print("-------------------------------------")

    filtered_df = df[df['tache'].str.strip() != 'scheduled_notification_job']
    info_counts_filtered = filtered_df['tache'].value_counts()

    task_percentages = (info_counts_filtered / len(df)) * 100

    task_table = pd.DataFrame({'Tâche': task_percentages.index, 'Pourcentage': task_percentages.values})
    task_table = task_table.sort_values('Pourcentage', ascending=False)

    print(task_table)

    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
    output_filename = f"output_data_{formatted_datetime}.csv"

    df.to_csv(path_or_buf=f"../../data/datasets/{output_filename}", index=False)

    end_time = time.time()
    total_time_sec = end_time - start_time
    minutes, secondes = divmod(total_time_sec, 60)

    print(f"Ligne(s) {line_count} traitée(s)")
    print("Temps total d'exécution :", minutes, "minute(s) et ", round(secondes), "secondes")

#process_logs(logs=logs)