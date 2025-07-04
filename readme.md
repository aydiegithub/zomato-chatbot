# Zomato Chatbot

A portfolio project demonstrating a Zomato-style chatbot built with ChainLit and Groq API. This interactive assistant guides users through food ordering, handles menu queries, calculates totals, and simulates payment — all in a short, friendly conversational flow.

## Features

- **Interactive Chat UI** powered by [ChainLit](https://github.com/chainlit/chainlit)
- **Lightweight LLaMA inference** via [Groq API](https://groq.com)
- **Retrieval of dynamic menu sections** for efficient token usage
- **Order collection** with item confirmation, pickup/delivery flow, address capture, and summary pricing
- **Error handling** and history trimming to stay within token limits

## Tech Stack

- Python 3.9+
- [ChainLit](https://github.com/chainlit/chainlit)
- [requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Repository Structure

```
├── app.py              # ChainLit frontend integration
├── src
    └── llm.py          # Groq API call logic and message handling
│   └── prompt.py       # system_instruction definition
├── requirements.txt    # Python dependencies
└── chainlit.md         # Chat UI customisation markdown
```

## Getting Started

Follow these steps to run the chatbot locally:

1. **Clone the repository**

   ```bash
   git clone https://github.com/aydiegithub/zomato-chatbot.git
   cd zomato-chatbot
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a **``** file** in the project root:

   ```env
   GROQ_API_KEY=hf_your_groq_api_key_here
   ```

4. **Run the ChainLit app**

   ```bash
   chainlit run app.py
   ```

5. **Open your browser** at `http://localhost:8000` to interact with the bot.

## Usage

- Type messages like:

  - `Hi! I want to order a pizza.`
  - `Show me burger options.`
  - `I’d like two Paneer Tikka Pizzas and a Coke.`

- The bot will guide you through confirming items, asking for pickup/delivery, capturing address, and summarizing your order with total cost.

## Socials & Links

- Website: [Aydie’s Avenue](https://aydie.in)
- LinkedIn: [Aydie Music](https://www.linkedin.com/in/aydiemusic)
- Instagram: [Aydie Music](https://www.instagram.com/aydiemusic)
- YouTube: [AydieMusic](https://www.youtube.com/AydieMusic)
- GitHub: [aydiegithub](https://github.com/aydiegithub)
- GitLab: [aydie](https://gitlab.com/aydie)
- LeetCode: [aydie](https://leetcode.com/aydie)
- HackerRank: [aydie](https://www.hackerrank.com/aydie)

---

**© 2025 Aydie Bantai. All rights reserved.**
