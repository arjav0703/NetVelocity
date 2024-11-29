# NetVelocity - Network Speed Test Application

**NetVelocity** is a simple network speed test application built using Python's `Tkinter` library for the graphical user interface (GUI) and the `speedtest-cli` module to measure internet speed. This app measures your download speed, upload speed, and latency (ping), and displays the results in a visually appealing GUI.

## Click below to watch Demo

[![Watch the video](https://cloud-8tnhv5zez-hack-club-bot.vercel.app/0image.png)](https://cloud-4zusmpzfz-hack-club-bot.vercel.app/0screencast_from_2024-11-29_17-19-09.mp4)

## Features

- **Ping (Latency)**: Displays the ping in milliseconds (ms).
- **Download Speed**: Measures and displays the download speed in Megabits per second (Mbps).
- **Upload Speed**: Measures and displays the upload speed in Megabits per second (Mbps).
- **Interactive Button**: The "Start Test" button triggers the speed test and updates the results on the GUI.
- **Minimal and clean design**: The application provides a user-friendly interface with an intuitive layout.

## Requirements

To run this application, you need the following:

- **Python 3.x**: Make sure Python 3.x is installed on your system.
- **Tkinter**: Python's built-in library for GUI development (it should be installed by default with Python).
- **speedtest-cli**: A Python library used to test internet speeds.

### Install Required Libraries

1. Install `speedtest-cli` using `pip`:
   ```bash
   pip install speedtest-cli
   ```

## How to Run

1. **Download/Clone the Project**:
   - Download the source code files or clone this repository using:
     ```bash
     git clone https://github.com/arjav0703/NetVelocity.git
     ```


2. **Run the Application**:
   - Open a terminal/command prompt in the project directory and run:
     ```bash
     python3 ./NetVelocity/main.py
     ```
   - This will launch the application window, and you can click on the "Start Test" button to begin the speed test.

## How It Works

1. **Speed Test Execution**:
   - The `test()` function calls the `speedtest.Speedtest()` class to check:
     - **Download Speed**: Measured in Mbps (Megabits per second).
     - **Upload Speed**: Measured in Mbps.
     - **Ping (Latency)**: Measured in milliseconds (ms).
   - The values are then displayed on the GUI in their respective labels.

2. **GUI Updates**:
   - Once the test is complete, the download speed, upload speed, and ping are updated dynamically on the screen.
   - The results are displayed in real-time using Tkinter's `Label` widgets.


## Troubleshooting

- **Issue**: If you see an error like "No module named 'speedtest'":
  - Solution: Install the `speedtest-cli` library using `pip install speedtest-cli`.

- **Issue**: The application doesn't display the correct result:
  - Solution: Ensure that your internet connection is active and working correctly before testing.

## License

This project is open-source and available under the MIT License.

## Acknowledgments
- https://www.youtube.com/watch?v=duNlmdYXXVE&list=PLl316cKxhMxtOWHa88kDqm42uWz1aqGfD&index=28&t=1088s
- The app uses the `speedtest-cli` Python package to measure internet speeds.
- Thanks to the Tkinter library for providing a simple and easy-to-use way to create GUIs in Python.