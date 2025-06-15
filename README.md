# 🌧️ Rain Alert – Daily Weather-Based Umbrella Reminder

**Rain Alert** is a lightweight Python project that checks the weather daily using the [OpenWeatherMap API](https://openweathermap.org/api) and alerts registered users via email if it's likely to **rain or snow**. It's a simple automation script hosted on [PythonAnywhere](https://www.pythonanywhere.com/) and designed to send timely umbrella reminders every morning.

---

## 📌 Overview

Every morning at **7:00 AM**, the system:
1. Queries the weather for a **fixed latitude and longitude**.
2. Parses the API response for weather conditions.
3. If rain or snow is predicted:
   - Sends an email to all users in the mailing list with a reminder to carry an umbrella ☔

---

## 📁 Project Structure

RainAlert/
├── main.py # Handles weather data fetching and decision logic
├── SendEmail.py # Manages email sending via SMTP
└── README.md

---

## 🔧 How It Works

- **Weather API Integration**:  
  Connects to OpenWeatherMap One Call API using a static lat/lon to retrieve daily weather data.

- **Rain Detection Logic**:  
  Scans the response for rain/snow indicators (e.g., `"rain"`, `"snow"` in weather condition descriptions).

- **Email Notification**:  
  Uses Python's built-in `smtplib` to send emails to a list of recipients.

- **Deployment**:  
  Runs daily via a scheduled task on [PythonAnywhere](https://www.pythonanywhere.com).

---

## 🧪 Example

### Weather API Output Snippet:
```json
"weather": [
  {
    "id": 500,
    "main": "Rain",
    "description": "light rain"
  }
]
```

## Run Manually:
```bash
python main.py
```

