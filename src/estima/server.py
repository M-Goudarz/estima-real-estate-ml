import uvicorn


def main() -> None:
    """Run the Estima API server."""
    uvicorn.run(
        "estima.api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    main()