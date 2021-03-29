from datetime import datetime
import csv

def ack1(M, N):
    return (N + 1) if M == 0 else (
        ack1(M-1, 1) if N == 0 else ack1(M-1, ack1(M, N-1)))


def test():
    start = datetime.now()
    #print(0, 5)
    #print(f'Result: {ack1(0, 5)}')
    end = datetime.now()
    delta = end - start

    return f'{delta.total_seconds():.3f}s'


test_result = test()

with open('results.csv', mode='w') as csv_file:
    fieldnames = ['Language', 'Test Name', 'Input', 'Time']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Language': 'python', 'Test Name': 'ackermann-recurssive', 'Input': '(0 & 5)','Time': test_result})

with open('results.csv','r', newline='') as file:
    reader = csv.reader(file, delimiter=',', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(f'{row[0]:<15}  {row[1]:<20} {row[2]:<15} {row[3]:<15}')