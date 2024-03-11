import statistics

def statistical_calculator(data):
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
            "Variance": variance_value
        }

        return result

    except statistics.StatisticsError as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Example usage:
    data = [2, 4, 4, 4, 5, 5, 7, 9]
    result = statistical_calculator(data)

    if isinstance(result, dict):
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print(result)
