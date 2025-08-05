# 🎬 IMDB Review Sentiment Analysis

This is a simple web application built using **TensorFlow**, **Keras**, and **Streamlit** that predicts the sentiment (Positive/Negative) of a movie review entered by the user. It uses a pre-trained RNN (Recurrent Neural Network) model trained on the IMDB movie reviews dataset.

---

## 🚀 Features

- Input a movie review and get sentiment prediction in real-time.
- Built using `SimpleRNN` from TensorFlow.
- Clean and interactive web interface using Streamlit.
- Loads a pre-trained model (`model.h5`).

---

## 🛠 Tech Stack

- Python
- TensorFlow / Keras
- NumPy
- Streamlit

---

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Aditya-Tyagi-05/imdb-sentiment-analysis-simplernn.git
   cd imdb-sentiment-analysis
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure you have the model file**:
   Make sure `model.h5` is placed in the same directory.

4. **Run the app**:
   ```bash
   streamlit run app.py
   ```

---

## 📁 Project Structure

```
├── app.py              # Main Streamlit app
├── model.h5            # Pre-trained sentiment analysis model
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

## 💡 How It Works

1. The user inputs a movie review.
2. The app tokenizes and pads the input based on IMDB word index.
3. The pre-trained RNN model predicts sentiment.
4. The sentiment is displayed as **Positive** or **Negative** with confidence.

---



---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/)

---

## ✨ Author

- [Aditya-Tyagi-05](https://github.com/Aditya-Tyagi-05)
