import tkinter as tk
from tkinter import scrolledtext
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load movie data
movies = pd.read_csv('movies.csv')
movies['tags'] = movies['overview'] + movies['genre']
new_data = movies[['id', 'title', 'tags']]

# Create CountVectorizer and compute similarity matrix
cv = CountVectorizer(max_features=10000, stop_words='english')
vector = cv.fit_transform(new_data['tags'].values.astype('U')).toarray()
similarity = cosine_similarity(vector)

# Tkinter GUI
def recommend_movie():
    user_input = entry.get()
    similar_movies = recommend(user_input)
    display_result(similar_movies)

def recommend(movie_title):
    index = new_data[new_data['title'] == movie_title].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    similar_movies = [new_data.iloc[i[0]].title for i in distance[1:6]]
    return similar_movies

def display_result(similar_movies):
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Movies similar to '{entry.get()}':\n")
    for movie in similar_movies:
        result_text.insert(tk.END, f"{movie}\n")
    result_text.config(state=tk.DISABLED)

# Create main window
window = tk.Tk()
window.title("Movie Recommendation System")
window.config(bg='#070B15')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 500
window_height = 400
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Set window size and position
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create GUI components
label = tk.Label(window, text="Enter a movie title:",font=('Inter', 20))
label.pack(pady=10)
label.config(fg='#F1F5F9')
label.config(bg='#070B15')

entry = tk.Entry(window,bg='white', fg='#475569', width=20,font=('Inter', 16))
entry.pack(pady=10)

recommend_button = tk.Button(window, text="Recommend Movies", bg='#FBBF24', fg='#070B15', command=recommend_movie)
recommend_button.pack(pady=10)

result_text = scrolledtext.ScrolledText(window, width=50, height=10, state=tk.DISABLED)
result_text.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
