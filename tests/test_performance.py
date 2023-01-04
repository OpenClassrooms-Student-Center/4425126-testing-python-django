from locust import HttpUser, task

class ProjectPerfTest(HttpUser):
    @task
    def home(self):
        self.client.get("home/")

    @task
    def redirect_home(self):
        self.client.get("")

    @task
    def login(self):
        self.client.get("user/login")

    @task
    def signup(self):
        self.client.get("user/signup")

    @task
    def logout(self):
        self.client.get("user/logout")

    @task
    def change_password(self):
        self.client.get("user/change-password")

    