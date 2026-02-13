from backend.config.dask_config import create_dask_client
import time

def main():
    print("Main started")

    client = create_dask_client()

    print(client)
    print(f"Dashboard: {client.dashboard_link}")

    print("Cluster running... Press CTRL+C to stop")

    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
