def total_salary(path: str) -> str:
    count = 0
    sum = 0

    try:
        with open(path, "r", encoding="utf-8") as fh:
            while True:
                line = fh.readline()
                if not line:
                    break
                count += 1
                sum += int(line.split(",")[1])
    except FileNotFoundError:
        return "Error: File not found"

    return f"Total Salary: {sum}, Average Salary: {sum/count}"
