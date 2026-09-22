def save_results(file, txt):
    with open(file, "a", encoding="utf-8") as file:
        for i in txt:
            file.write(str(i) + "\n")