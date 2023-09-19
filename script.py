import os
import sqlite3


def add_images_to_db(path):
    dir_list = os.listdir(path)
    conn = sqlite3.connect("my_images.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS images (
                    id INTEGER PRIMARY KEY,
                    image_name TEXT,
                    image_data BLOB,
                    score REAL
                )''')
    total_images = len(dir_list)
    curr_count = 1
    for image in dir_list:
        score = 1000  # initial score
        with open(f"{path}/{image}", 'rb') as file:
            print(f"reading image {image}, {curr_count} of {total_images}...")
            image_data = file.read()
            image_name_split = image.split(".")
            image_name = "_".join(image_name_split[0:len(image_name_split)-1])
            conn.execute("INSERT INTO images (image_name, image_data, score) VALUES (?, ?, ?)",
                         (image_name, sqlite3.Binary(image_data), score))
            conn.commit()
        curr_count += 1
    conn.close()


def main():
    path = "/Users/aaryamann/code/hot_or_not/misc/images"
    add_images_to_db(path)


if __name__ == "__main__":
    main()
