from subprocess import Popen, PIPE

with Popen(['python', 'lektion_1_opgaver/11,3/producer.py'], stdout=PIPE, text=True) as process:
    for x in process.stdout:
        print(x)