import csv

def read_csv_file(file_path):
    file = open(file_path, "r", encoding="utf-8", errors="", newline="")
    csv_file = csv.reader(file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    return csv_file

def write_csv_file(file_path, header, body):
    with open(file_path, 'w', encoding='utf-8', newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        writer.writerow(header)
        writer.writerows(body)
    csv_file.close()

def check_address(mail_address):
    return (
        mail_address != '' and
        not '@sora-michi.com' in mail_address and
        not '@everforth.co.jp' in mail_address and
        # not '@ledian.jp' in mail_address and
        not 's.m.m.y.ito+' in mail_address and
        not 'masaru_nagaishi+' in mail_address
    )

def chech_name(name):
    return (
        not 'テスト' in name
    )