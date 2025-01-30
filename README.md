# Book Recommendation System
![Book Recommendation](https://github.com/user-attachments/assets/e5b36ea3-66b7-427e-b2d4-1041c9acc595)

## 📌 Overview
This project is a **Book Recommendation System** that provides personalized book suggestions based on:
- **Popularity-Based Recommendation**: Suggests books that are widely liked by users.
- **Collaborative Filtering**: Provides recommendations by analyzing user preferences and similarities.

## 🚀 Features
- Search for books by title.
- Get recommendations based on book popularity.
- Personalized recommendations using collaborative filtering.
- Interactive web interface built with Flask and Bootstrap.

## 🛠️ Technologies Used
- **Programming Languages**: Python, JavaScript
- **Backend**: Flask
- **Database**: MySQL, MongoDB
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-Learn
- **Frontend**: HTML, CSS, Bootstrap

## 📂 Project Structure
```
📁 Book-Recommendation-System
│── 📄 app.py                # Main Flask application
│── 📄 popular.pkl           # Precomputed popularity-based recommendations
│── 📄 pt.pkl                # Pivot table for collaborative filtering
│── 📄 books.pkl             # Dataset of books
│── 📄 similarity_score.pkl  # Similarity matrix for recommendations
│── 📂 templates             # HTML templates
│   │── index.html           # Home page
│   │── rec.html             # Recommendation page
│── 📂 static                # Static files (CSS, JS, images)
```

## 🔥 How to Run
1. Clone the repository:
   ```sh
   git clone https://github.com/GauravRavan/book-recommendation.git
   ```
2. Navigate to the project directory:
   ```sh
   cd book-recommendation
   ```
3. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```sh
   python app.py
   ```
5. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## 📊 Screenshots
### 🔹 Home Page
![Home Page](https://github.com/user-attachments/assets/e5b36ea3-66b7-427e-b2d4-1041c9acc595)

### 🔹 Recommendation Page
![Recommendation Page](https://github.com/user-attachments/assets/9a8c7500-fe34-4b2a-bbf9-9261b994d16f)

## 📌 Future Enhancements
- Improve recommendation accuracy using deep learning models.
- Add user authentication for personalized recommendations.
- Deploy on cloud platforms like AWS or Heroku.

## 🤝 Contributing
Feel free to fork this repository and submit pull requests for any improvements or additional features!
