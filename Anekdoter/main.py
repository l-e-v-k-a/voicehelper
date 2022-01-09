import sqlite3
import requests
import time
from auth_data import token


def write_db(data):
    conn = sqlite3.connect('i_have_reached_comedy.db')
    cur = conn.cursor()
    for joke in data:
        cur.execute(f"""INSERT INTO jokes (id, text, likes) VALUES {joke['id'], joke['text'], joke['likes']};""")
    conn.commit()


def get_all_posts_ids():
    conn = sqlite3.connect('i_have_reached_comedy.db')
    cur = conn.cursor()
    ids = cur.execute(f"""SELECT id from jokes ORDER BY -id""")
    conn.commit()
    result = [i[0] for i in list(ids)]  # [(1,), (2,), (3,)] --> [1, 2, 3]
    return result


def get_wall_posts(group_name="anekdotikategoriib"):
    counter = 0

    url = f"https://api.vk.com/method/wall.get?domain={group_name}&count=100&access_token={token}&v=5.81"
    req = requests.get(url)
    src = req.json()
    time.sleep(0.5)

    posts_count = src["response"]["count"]

    for offset in range(0, posts_count+100, 100):
        if counter >= posts_count:
            break
        url = f"https://api.vk.com/method/wall.get?domain={group_name}&count=100&access_token={token}&v=5.81&offset={offset}"
        req = requests.get(url)
        src = req.json()

        # Получаем данные из постов
        posts = src["response"]["items"]

        for post in posts:
            if not(int(post["id"]) in get_all_posts_ids()):
                if (post["text"] != "") and (not "http" in post["text"]) and (not "attachments" in post) and (not "copy_history" in post):
                    print("id Поста: ", post["id"])
                    print(post["text"].replace("\n.\n", "").replace("\n\n", "\n").strip())
                    print(post["likes"]["count"], "Лайков")

                    joke = {
                        "id": int(post["id"]),
                        "text": post["text"].replace("\n.\n", "").replace("\n\n", "\n").strip().replace("'", ''),
                        "likes": int(post["likes"]["count"])
                    }
                    write_db([joke])
                else:
                    print("Реклама, картинка или репост")
            else:
                return
            counter += 1
            print("Обработано постов: ", counter, "\n")

        time.sleep(0.334)


def get_random_joke(format_by_width=True):
    conn = sqlite3.connect('i_have_reached_comedy.db')
    cur = conn.cursor()
    joke = list(cur.execute("""SELECT * FROM jokes ORDER BY RANDOM() LIMIT 1;"""))[0][1].replace("\\n", "\n")
    conn.commit()
    if format_by_width:
        import textwrap
        return textwrap.fill(joke, 60)
    return joke


print(get_random_joke())
