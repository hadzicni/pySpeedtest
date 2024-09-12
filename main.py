import speedtest

def run_speedtest():
    st = speedtest.Speedtest()

    print("Choose the best server...")
    st.get_best_server()

    print("Test Download-Speed...")
    download_speed = st.download() / 1_000_000 
    print("Test Upload-Speed...")
    upload_speed = st.upload() / 1_000_000 
    ping = st.results.ping

    print(f"Ping: {ping} ms")
    print(f"Download: {download_speed:.3f} Mbit/s")
    print(f"Upload: {upload_speed:.3f} Mbit/s")

if __name__ == "__main__":
    run_speedtest()
