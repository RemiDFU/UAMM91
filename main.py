from src.utils.helper_functions import open_csv_file
from scripts.data_exploration import plot_info_frequency, plot_task_distribution, plot_temporal_activity, display_log_statistics
from src.data_preprocessing.data_cleaning import process_logs

def preprocess_data(data):

    """
    Effectuez le prétraitement des données ici
    Nettoyez, encodez, normalisez, etc.
    """
    logs = []

    with open("data/rawData/worker-c840_21_11_2023.log", "r", encoding="utf-8") as file:
        logs = file.readlines()[:3]
    process_logs(logs)


def load_data(file_path):
    data = open_csv_file(file_path)
    return data


def explore_data(data):

    plot_info_frequency(data)

    plot_task_distribution(data)

    plot_temporal_activity(data)

    display_log_statistics(data)


def build_model(data):
    """
    """


def evaluate_model(model, data):
    """
    """


def visualize_results(data):
    """
    """


def main():
    # preprocessed_data = preprocess_data(data)
    file_path = 'data/datasets/output_data_2023-12-10_17-06-11.csv'
    data = load_data(file_path)
    print(data.head())
    if data is not None:
        explore_data(data)

        model = build_model(data)

        evaluate_model(model, data)

        visualize_results(data)


if __name__ == "__main__":
    main()
