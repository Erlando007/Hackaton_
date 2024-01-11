import requests


class AuthUser:
    def __init__(self,username,password):
        self.auth_token = None
        self.username = username
        self.password = password
    
    def authenticate_user(self):
        api_url = 'http://127.0.0.1:8000/account/auth/token/login/' 
        data = {
            'username': self.username,
            'password': self.password,
        }

        try:
            response = requests.post(api_url, data=data)
            if response.status_code == 200:
                token = response.json().get('auth_token')
                self.auth_token = token
                return f"Успешная авторизация! Токен: {token}"
            else:
                return f"Ошибка авторизации. Статус код: {response.status_code}"
                
        except Exception as e:
            return f"Произошла ошибка: {str(e)}"
    def get_ankets(self):
        header = {'Authorization':'Token ' + self.auth_token}
        api_url = 'http://127.0.0.1:8000/rec_ankets/'
        response = requests.get(headers=header,url=api_url)
        return response.text