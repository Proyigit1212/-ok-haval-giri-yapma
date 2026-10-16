def initialize_users():
    """Başlangıç kullanıcı sözlüğünü döndürür."""
    return {}

def add_user(users, username, password):
    """
    Kullanıcıyı sözlüğe ekler. 
    Eğer kullanıcı zaten varsa hata mesajı döner, yoksa ekleyip başarılı mesajı döner.
    """
    if username in users:
        return "Kullanıcı zaten mevcut."
    
    users[username] = password
    return f"Yeni kullanıcı {username} başarıyla eklendi."