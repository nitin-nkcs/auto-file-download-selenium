# Auto File Download with Selenium

This project demonstrates how to automate file downloads using Selenium WebDriver in Python.

## Getting Started

### Prerequisites

- Python 3.x
- Selenium
- WebDriver for your browser (e.g., ChromeDriver for Google Chrome)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/nitin-nkcs/auto-file-download-selenium.git
    ```
2. Navigate to the project directory:
    ```bash
    cd auto-file-download-selenium
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Adding ChromeDriver to System PATH

To ensure ChromeDriver is accessible, add it to your system PATH:

#### Windows:
1. Download ChromeDriver from the official site.
2. Extract the `chromedriver.exe` to a directory of your choice, e.g., `C:\bin`.
3. Add the directory to the PATH:
    - Press `Win + R`, type `sysdm.cpl`, and press Enter.
    - Go to the **Advanced** tab and click on **Environment Variables**.
    - Under **System variables**, find the `Path` variable and click **Edit**.
    - Click **New** and add the path to the directory where you extracted `chromedriver.exe` (e.g., `C:\bin`).
    - Click **OK** to close all windows.

#### macOS:
1. Download ChromeDriver from the official site.
2. Extract the `chromedriver` file to a directory of your choice, e.g., `~/bin`.
3. Add the directory to the PATH:
    - Open Terminal.
    - Open your shell configuration file in a text editor (e.g., `nano ~/.bash_profile` or `nano ~/.zshrc`).
    - Add the following line to the file:
      ```sh
      export PATH="$PATH:~/bin"
      ```
    - Save the file and run `source ~/.bash_profile` or `source ~/.zshrc` to apply the changes.

#### Linux:
1. Download ChromeDriver from the official site.
2. Extract the `chromedriver` file to a directory of your choice, e.g., `/usr/local/bin`.
3. Add the directory to the PATH:
    - Open Terminal.
    - Open your shell configuration file in a text editor (e.g., `nano ~/.bashrc` or `nano ~/.zshrc`).
    - Add the following line to the file:
      ```sh
      export PATH="$PATH:/usr/local/bin"
      ```
    - Save the file and run `source ~/.bashrc` or `source ~/.zshrc` to apply the changes.

### Usage

1. Update the `config.py` file with your download directory and other settings.
2. Run the script:
    ```bash
    python download_script.py
    ```

### Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

### License

This project is licensed under the MIT License - see the LICENSE file for details.
