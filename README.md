# PPC || Exercices to understand Python Processes/Threads/Multiprocessing/MultiThreads  

## TD1 || Process/Signal/Pipe
Usage: 
```bash
python3 <script.py> <args>
```

How to see process:

```bash
ps -ax
ps -ax | grep <script.py>
htop
```

## TD2 || SharedMemory/MessagePassing
Usage exo1:
```bash
python3 exo1.py <args>
```

Usage Message passing demo:
```bash
pip3 install sysv_ipc
python3 exampleServer.py 
python3 exampleClient.py
```

To kill Server:
```bash
ps -ax | grep exampleServer.py
kill <PID above of exampleServer.py>
```

Usage exo2:
```bash
server.py
client.py
```

Troubleshooting:
[Doc Sysv_ipc](http://semanchuk.com/philip/sysv_ipc/#message_queue)

```bash
ipcs
htop
```

## TD3 || Threads/MultiThreading
Usage:
```bash
python3 example.py <int>
python3 exo1.py <int>
python3 exo2*.py
```




## License

[MakeReadMe](https://www.makeareadme.com/)
