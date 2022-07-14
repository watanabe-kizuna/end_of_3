import glob
import my_lib


member_ids          = []

old_csv_path        = 'C:/Users/aqtor/Desktop/ledian_csv/end_of_3/old'
new_csv_path        = 'C:/Users/aqtor/Desktop/ledian_csv/end_of_3/new'
exc_csv_path        = 'C:/Users/aqtor/Desktop/ledian_csv/end_of_3/exc'

user_files          = glob.glob(f'{old_csv_path}/user/*')
subscription_files  = glob.glob(f'{old_csv_path}/subscription/*')
order_files         = glob.glob(f'{old_csv_path}/order/*')

member_id_index     = 0
last_name_index     = 3
first_name_index    = 4
mail_address_index  = 10


def rebuild_user_csv():
    exc_header = []
    exc_body = []
    for file in user_files:
        file_name = str(file).split('\\')[1]
        csv_file = my_lib.read_csv_file(file)
        header = next(csv_file)
        exc_header = header
        body = []

        for row in csv_file:
            member_id = row[member_id_index]
            last_name = row[last_name_index]
            first_name = row[first_name_index]
            mail_address = row[mail_address_index]

            if my_lib.check_address(mail_address) and my_lib.chech_name(last_name) and my_lib.chech_name(first_name):
                body.append(row)
            else:
                row.insert(0, file_name.replace("production_", ""))
                exc_body.append(row)
                member_ids.append(member_id)
        
        my_lib.write_csv_file(f'{new_csv_path}/user/{file_name.replace("production_", "")}', header, body)
    
    exc_header.insert(0, "ファイル名")
    my_lib.write_csv_file(f'{exc_csv_path}/user/exc_users.csv', exc_header, exc_body)

def main():
    rebuild_user_csv()

if __name__ == "__main__":
    main()
