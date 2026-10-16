# user_management.py

def initialize_users():
    """Önceden tanımlanmış kullanıcı sözlüğünü döndürür"""
    return {
        "user1": "password1",
        "user2": "password2",
        "user3": "password3",
        "user4": "password4",
        "user5": "password5",
    }

def add_user(users, username, password):
    """Kullanıcı sözlüğünde kullanıcı mevcut değilse, yeni kullanıcı ekler.
    Güncellenmiş kullanıcı sözlüğünü döndürür."""
    # Görev: Eğer kullanıcı zaten varsa şu mesajı döndür - "Bu girişe sahip bir kullanıcı zaten mevcut."
    # Görev: Eğer kullanıcı sözlükte yoksa, kullanıcı adını anahtar, şifreyi değer olarak sözlüğe yeni bir giriş ekleyin.
    return f"Yeni kullanıcı {username} başarıyla eklendi."

def display_users(users):
    """Tüm kullanıcıları ve şifrelerini listeler."""
    print("Sistemde halihazırda kayıtlı kullanıcılar ve şifreleri:")
    for username, password in users.items():
        print(f"Kullanıcı adı: {username}, Şifre: {password}")

def main():
    users = initialize_users()
    display_users(users)

    print("\nYeni bir kullanıcı ekleyebilirsiniz.")
    username = input("Yeni kullanıcı adını girin: ")
    password = input("Yeni kullanıcının şifresini girin: ")
    result = add_user(users, username, password)
    print(result)

    print("\nYeni kullanıcı eklendikten sonraki tüm kullanıcı listesi:")
    display_users(users)

if __name__ == "__main__":
    main()
