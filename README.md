# WhatsApp Vertical Spam Script

A specialized Python automation script designed to send a high volume of sequential messages to a single WhatsApp contact using browser-based automation layers.

## Overview

This tool automates rapid message delivery targeting a single designated phone number. It cycles continuously through a list of text variations over a defined loop range inside a clean, modular execution architecture, making it useful for communication testing, notification system stress verification, or high-frequency automated alerts.

## Features

- **Standardized Execution Layer:** Wrapped cleanly inside a modular `main()` function with a standard `__main__` entry guard to prevent execution side effects upon cross-module integration.
- **Targeted Single-Number Delivery:** Routes all outgoing message configurations continuously to one specified recipient profile.
- **High-Volume Loop Execution:** Configured via an adjustable runtime counter loop to send hundreds or thousands of messages in a single continuous session.
- **Dynamic Text Cycling:** Alternates through available items in the `messages` array based on incremental index configurations to vary delivery payloads.
- **Real-Time Transmission Tracker:** Prints the active counter index value (`i`) straight to the command line console upon every loop execution pass.
- **Inline Error Recovery:** Safely catches automation delivery bugs or browser timeout anomalies within individual loop cycles, preventing total runtime failures.

## Project Structure

```bash
whatsapp-stress-tester/
├── main.py              # Modular automation script containing the execution loop
├── requirements.txt     # Dependency tracking file (requires pywhatkit)
└── README.md            # Script documentation and usage guide
```

## Setup & Execution

### Prerequisites

- Python 3.7+ environment configured on the execution machine.
- An open default browser instance securely logged into **WhatsApp Web** prior to running the utility.

### Installation

- Clone or download this project folder layout:

  ```bash
  git clone https://github.com
  ```

- Navigate into the target project folder and install the required library dependency:
  ```bash
  pip install -r requirements.txt
  ```

### Configuration & Usage

1. Open `main.py` using your code editor.
2. Provide the complete destination international value within `phone_number` (e.g., `+964xxxxxxxxxx`).
3. Set your target message strings in the `messages` array pool.
4. Modify the loop iteration ceiling value in `range(1000)` to specify the exact transmission limit.
5. Boot up the message execution loop through your command shell terminal:
   ```bash
   python main.py
   ```

## Author

H2SO4-1191 – Software Engineer
