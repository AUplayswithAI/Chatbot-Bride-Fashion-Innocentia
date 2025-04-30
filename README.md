# BridalBot – AI-powered WhatsApp Chatbot for a Bridal Dress Manufacturer

BridalBot is an intelligent chatbot designed to assist customers of a bridal dress manufacturer via WhatsApp. It handles common inquiries such as orders, reorders, order modifications, complaints, deliveries, and product-related questions using OpenAI's GPT-4.

---

## 🎯 Features

- Automates responses to frequently asked customer questions:
  - New orders & reorders
  - Order modifications
  - Complaints and returns
  - Shipping and delivery updates
  - Product info (sizing, materials, production time, customizations)
- Integrated with WhatsApp using the Twilio API
- Natural language processing with OpenAI GPT-4

---

## ⚙️ Technologies

- Python 3.x
- Flask
- Twilio WhatsApp API
- OpenAI GPT-4
- `python-dotenv` for environment variable management

---

## 🚀 Setup Instructions

### 1. Clone the repository and create a virtual environment

```bash
git clone https://github.com/your-username/whatsapp-bridalbot.git
cd whatsapp-bridalbot
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
