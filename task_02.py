def get_cats_info(path: str) -> list[dict[str, str]]:
    result = []
    try:
        with open(path, "r", encoding="utf-8") as fh:
            while True:
                line = fh.readline()
                if not line:
                    break
                
                id, name, age = line.strip().split(",")
             
                result.append({"id": id, "name": name, "age": age})
    except FileNotFoundError:
        return "Error: File not found"
    
    return result

