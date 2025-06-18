

def FileLogger(data):
    with open('logs.txt' , 'a') as f:
        f.write(data + '\n')

