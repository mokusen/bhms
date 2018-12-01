import csv

def create_list():
    """
    課金れ履歴のデータリストを作成する

    Returns
    -------
    base_list : list型
        課金履歴のデータリストを格納してあるcsvからlistを作成する
    """

    # 対象ファイル名(実行ディレクトリはmain.pyである)
    base_meta_name = "課金履歴.csv"
    with open(base_meta_name, newline='', encoding="shiftjis") as before:
        reader = csv.reader(before)
        base_list = []
        for row in reader:
            add_list = []
            add_list.append(int(row[0]))
            add_list.append(row[1])
            add_list.append(int(row[2]))
            add_list.append(int(row[3]))
            add_list.append(int(row[4]))
            base_list.append(add_list)
    return base_list