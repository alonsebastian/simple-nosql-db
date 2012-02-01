import backend

if __name__ == "__main__":
    for number in range(100):
        number = str(number) * 5
        backend.write_to_db(number)
