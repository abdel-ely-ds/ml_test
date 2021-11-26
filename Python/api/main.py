import uvicorn


def main():
    entry_point = "Python.api.api:app"
    uvicorn.run(entry_point, host="0.0.0.0", port=12345, reload=True)


if __name__ == "__main__":
    main()
