import statistics
from typing import List, Dict, Union


def statistical_calculator(data: List[int]) -> Dict[str, Union[float, str]]:
    """
    Calculates statistical measures for a list of numbers.

    Args:
        data: A list of numerical data points.

    Returns:
        A dictionary containing the mean, median, mode, standard deviation, and variance of the data.
        In case of errors during calculation, returns an error message as a string.
    """
    try:
        mean_value = statistics.mean(data)
        median_value = statistics.median(data)
        mode_value = statistics.mode(data)
        stdev_value = statistics.stdev(data)
        variance_value = statistics.variance(data)

        result = {
            "Mean": mean_value,
            "Median": median_value,
            "Mode": mode_value,
            "Standard Deviation": stdev_value,
            "Variance": variance_value,
        }

        return result

    except statistics.StatisticsError as e:
        return f"Error: {e}"


def save_result_to_file(
    result: Dict[str, Union[float, str]], filename: str = "output.txt"
) -> None:  # void
    """
    Saves the statistical results to a text file.

    Args:
        result: A dictionary containing statistical measures.
        filename: The name of the file to save the results to (default: 'output.txt').
    """
    with open(filename, "w") as file:
        for key, value in result.items():
            file.write(f"{key}: {value}\n")


if __name__ == "__main__":
    # Example usage:
    data: List[int] = [2, 4, 4, 4, 5, 5, 7, 9.0]
    result = statistical_calculator(data)

    if isinstance(result, dict):
        for key, value in result.items():
            print(f"{key}: {value}")

        # Save the result to a file
        save_result_to_file(result)
        print("Result saved to 'output.txt'")
    else:
        print(result)
