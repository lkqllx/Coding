import re
import sys

#
# string = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
# output = re.findall(r'[\w.-]+@[\w.-]+', string)
# if output:
#     print(output)
# else:
#     print('Not found')


def extract_names(html):
    file_year = re.findall(r'(\d{4})</h3>', html)
    male_names = re.findall(r'</td><td>(\w+)</td>', html)
    female_names = re.findall(r'[a-zA-Z]+</td><td>(\w+)</td>', html)
    names = male_names + female_names
    ranking = re.findall(r'<tr.*?><td>(\d+)', html)
    ranking = ranking * 2
    combination = list(zip(names, ranking))
    sorted_com = sorted(combination, key= lambda x: x[0])
    sorted_com = file_year + [f'{name} {rank}' for name, rank in sorted_com]
    text = '\n'.join(sorted_com)
    return text

def main():
    args = sys.argv[1:]

    if not args:
        print('usage --summaryfile file')
        sys.exit(1)

    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    if summary:
        with open(args[0], encoding='UTF-8') as f:
            html = f.read()
            extract_names(html=html)
    else:
        print('No summary file')
        sys.exit(1)

if __name__ == '__main__':
    main()

