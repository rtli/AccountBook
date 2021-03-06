import csv
import os


def init_second_classifier():
    c = set()

    if os.path.exists('classifier.csv'):
        with open('classifier.csv', 'r', encoding='UTF-8', newline='') as f:
            rows = csv.reader(f)
            for row in rows:
                if row[1] != '总支出':
                    c.add(row[0])
        l = list(c)
        l.sort(key=lambda x: len(x))
        return l
    else:
        with open('classifier.csv', 'w', encoding='UTF-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['示例二级分类',
                             '示例一级分类'])
            writer.writerow(['示例一级分类', '总支出'])
            return ['示例二级分类']


def init_first_classifier():
    if os.path.exists('classifier.csv'):
        c = set()
        with open('classifier.csv', 'r', encoding='UTF-8', newline='') as f:
            rows = csv.reader(f)
            for row in rows:
                if row[1] == '总支出':
                    c.add(row[0])
        l = list(c)
        l.sort(key=lambda x: len(x))
        return l
    else:
        with open('classifier.csv', 'w', encoding='UTF-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['示例二级分类',
                             '示例一级分类'])
            writer.writerow(['示例一级分类', '总支出'])
            return ['示例一级分类']


def get_last_line():
    if os.path.exists('spending.csv'):
        last = []
        with open('spending.csv', 'r', encoding='UTF-8', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                last = row
        return last
    else:
        with open('spending.csv', 'w', encoding='UTF-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['示例', '示例二级分类', 100])
            return ['示例', '示例二级分类', 100]


def write_spending(item, sort, price):
    from datetime import datetime
    item = str(datetime.now().month)+"."+str(datetime.now().day)+"-"+item
    with open('spending.csv', 'a', encoding='UTF-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([item, sort, price])


def delete_last_line():
    lines = list()
    with open('spending.csv', 'r', encoding='UTF-8', newline='') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
    if not row:
        return 0
    with open('spending.csv', 'w', encoding='UTF-8', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines[:-1])
    return 1


def update_classifier(second, first):
    new_line = [second, first]
    with open('classifier.csv', 'r', encoding='UTF-8', newline='') as f:
        rows = csv.reader(f)
        for row in rows:
            if(second in row):
                return 0
    with open('classifier.csv', 'a', encoding='UTF-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(new_line)
    return 1


def delete_classifier(items):
    exist = set()
    with open('classifier.csv', 'r', encoding='UTF-8', newline='') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            if row[0] in items or row[1] in items:
                exist.add(row[0])
                exist.add(row[1])

    with open('spending.csv', 'r', encoding='UTF-8', newline='') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            if row[1] in exist:
                return 0

    lines = list()
    with open('classifier.csv', 'r', encoding='UTF-8', newline='') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            if row[0] not in items and row[1] not in items:
                lines.append(row)

    with open('classifier.csv', 'w', encoding='UTF-8', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

    return 1
