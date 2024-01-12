import requests
import json

class AuthUser:
    def __init__(self,username,password):
        self.auth_token = None
        self.username = username
        self.password = password
        self.header = None
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
                self.header = {'Authorization':'Token ' + self.auth_token}
                return f"Успешная авторизация!", True
            else:
                return f"Ошибка авторизации. Статус код: {response.status_code}", False
                
        except Exception as e:
            return f"Произошла ошибка: {str(e)}",None
    
    def get_ankets(self):
        api_url = 'http://127.0.0.1:8000/rec_ankets/'
        response = requests.get(headers=self.header,url=api_url)
        resp = response.text
        result = json.loads(resp)
        return result
    
    def toggle_like(self,id_anket):
        api_url = f'http://127.0.0.1:8000/account/anket/{id_anket}/toggle_like/'
        response = requests.post(headers=self.header,url=api_url)
        return response.status_code
    
    
