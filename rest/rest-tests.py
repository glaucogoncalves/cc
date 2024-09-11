import requests
import json

def get_test(text, url):
    result = requests.get(url)
    print("=== Test: "+text+" === ")
    print(json.dumps(result.json(),indent=2))

def post_test(text, url, data):
    result = requests.post(url,json=data)
    print("=== Test: "+text+" === ")
    print(json.dumps(result.json(),indent=2))
    return result.json()

def put_test(text, url, data):
    result = requests.put(url,json=data)
    print("=== Test: "+text+" === ")
    print(json.dumps(result.json(),indent=2))

def delete_test(text, url):
    result = requests.delete(url)
    print("=== Test: "+text+" === ")
    print(json.dumps(result.json(),indent=2))

url_base = "http://localhost:5000/todo/api/v1.0"

get_test("Obter Lista de Tarefas",url_base+"/tasks")
get_test("Obter Tarefa 1",url_base+"/tasks/1")

json_data = {
    "title": "nova tarefa",
    "description": "uma tarefa nova e que deve ser feita"
}

data = post_test("Criar tarefa",url_base+"/tasks",json_data)
get_test("Obter Lista de Tarefas",url_base+"/tasks")

json_data = {
    "done": True
}
put_test("Atualizar tarefa", data["task"]["uri"], json_data)
get_test("Obter Tarefa Nova", data["task"]["uri"])

delete_test("Remover tarefa criada", data["task"]["uri"])
get_test("Obter Tarefa Nova", data["task"]["uri"])