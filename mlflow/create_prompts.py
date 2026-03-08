from mlflow import MlflowClient

client = MlflowClient("http://localhost:5000")

client.create_prompt("iris-clf1")
client.create_prompt("iris-clf2")
client.create_prompt("iris-clf3")
client.create_prompt("iris-clf4")
client.create_prompt("iris-clf5")
client.create_prompt("iris-clf6")

client.create_prompt_version("iris-clf1", "classify the iris. just give me the number")
client.create_prompt_version("iris-clf2", "you are a botanist. look at the numbers and tell me what flower it is")
client.create_prompt_version("iris-clf3", "input: 4 numbers. output: 0, 1 or 2. thats it")
client.create_prompt_version("iris-clf4", "lalala")
client.create_prompt_version("iris-clf5", "23.5, 2.3, 3.7, 9.0")
client.create_prompt_version("iris-clf6", "classify the iris. input: 4 numbers: 23.5, 2.3, 3.7, 9.0")

print("done")
