from labs.lab_7.Functions.api_client import ApiClient
from labs.lab_7.Functions.repository import Repository
from labs.lab_7.Functions.console_app import ConsoleApp

def main():
    base_url = "https://jsonplaceholder.typicode.com"
    api_client = ApiClient(base_url)
    repository = Repository(api_client)
    app = ConsoleApp(repository)
    app.run()

if __name__ == "__main__":
    main()
