import threading
import time

def tarefa_pesada(id, segundos=2):
    print(f"[Thread {id}] Iniciando tarefa por {segundos}s...")
    time.sleep(segundos)
    print(f"[Thread {id}] Tarefa finalizada.")

def executar_sem_threads():
    inicio = time.time()
    for i in range(4):
        tarefa_pesada(i)
    fim = time.time()
    print(f"Tempo total SEM threads: {fim - inicio:.2f} segundos")

def executar_com_threads():
    threads = []
    inicio = time.time()
    for i in range(4):
        t = threading.Thread(target=tarefa_pesada, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    fim = time.time()
    print(f"Tempo total COM threads: {fim - inicio:.2f} segundos")

if __name__ == "__main__":
    print("Executando tarefas sem threads:")
    executar_sem_threads()

    print("\nExecutando tarefas com threads:")
    executar_com_threads()
