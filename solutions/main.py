# # # from library import download_video


# # # def main():
# # #     url = input("Enter YouTube URL: ")
# # #     download_video(url)


# # # if __name__ == "__main__":
# # #     main()

# # from library import read_video_urls


# # def main():
# #     urls = read_video_urls("data/video_urls.csv")

# #     print(urls)


# # if __name__ == "__main__":
# #     main()

# import time
# from library import read_video_urls, download_video


# def main():
#     urls = read_video_urls("data/video_urls.csv")

#     total_start = time.perf_counter()

#     for url in urls:
#         start = time.perf_counter()
#         download_video(url)
#         end = time.perf_counter()

#         elapsed = round(end - start, 2)
#         print(f"Downloaded one video in: {elapsed}")

#     total_end = time.perf_counter()
#     serial_time = round(total_end - total_start, 2)

#     print(f"Serial execution: {serial_time}")

#     with open("reports/sequential_report.md", "w") as file:
#         file.write("# Report\n\n")
#         file.write("## Serial execution\n\n")
#         file.write(f"Total time: {serial_time} seconds\n\n")
#         file.write("## Complexity\n\n")
#         file.write("Time complexity: O(n), because the program downloads each video one by one.\n\n")
#         file.write("Space complexity: O(n), because the program stores the list of video URLs from the CSV file.\n")


# if __name__ == "__main__":
#     main()

import time
from multiprocessing import Pool
from library import read_video_urls, download_video


def main():
    urls = read_video_urls("data/video_urls.csv")

    # Keep your serial time from Phase 05 here
    serial_time = 0  # replace 0 with your Phase 05 time

    start = time.perf_counter()

    with Pool() as pool:
        pool.map(download_video, urls)

    end = time.perf_counter()
    parallel_time = round(end - start, 2)

    print(f"Parallel execution: {parallel_time}")

    if serial_time > 0:
        speed_improvement = round(((serial_time - parallel_time) / serial_time) * 100, 2)
    else:
        speed_improvement = 0

    with open("reports/sequential_report.md", "a") as file:
        file.write("\n\n## Parallel execution\n\n")
        file.write(f"Total time: {parallel_time} seconds\n\n")
        file.write("## Comparison\n\n")
        file.write(f"Speed improvement: {speed_improvement}%\n")


if __name__ == "__main__":
    main()