# viết chương trình python để thực hiện các yêu cầu HTTP đồng thời bằng các luồng tự tăng dần và các số lẻ khác theo thứ tự tăng dần đối với một ngưỡng nhất định
import threading
import requests

def send_request(url):
    try:
        response = requests.get(url)
        print(f"Response: {response.status_code}, {response.text}")
    except requests.RequestException as e:
        print(f"Error: {e}")

def main():
    url = "https://httpbin.org/get"
    thread_count = 10
    threads = [threading.Thread(target=send_request, args=(url,)) for _ in range(thread_count)]
    for t in threads: t.start()
    for t in threads: t.join()

if __name__ == "__main__":
    main()


