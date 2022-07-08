import pandas as pd
import glob

def check_address(mail_address):
    return (
        mail_address != 'nan' and
        not '@sora-michi.com' in mail_address and
        not '@everforth.co.jp' in mail_address and
        not '@ledian.jp' in mail_address and
        not 's.m.m.y.ito+' in mail_address
    )

def chech_name(name):
    return (
        not 'テスト' in name
    )

def main():
    files = glob.glob(f"C:/Users/aqtor/Desktop/ledian_csv/end_of_3/user/*")
    for file in files:
        csv_file = pd.read_csv(filepath_or_buffer=file, encoding="utf-8", sep=",")
        df_csv = pd.DataFrame(csv_file)
        
        file_name = str(file).split("\\")[1]
        print(f'=== {file_name} ===')

        row_num = 0
        for index, row in df_csv.iterrows():
            row_num += 1
            mail_address = str(row.loc['メールアドレス'])
            last_name = str(row.loc['姓（カナ）'])
            first_name = str(row.loc['名（カナ）'])

            if  check_address(mail_address) and chech_name(last_name) and chech_name(first_name):
                print(f'{row_num + 1}行目 {last_name} {first_name} {mail_address}')
        
        print()

if __name__ == "__main__":
    main()
