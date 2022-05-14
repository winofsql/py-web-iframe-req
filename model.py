from settings import *

# ***************************
# テーブル作成
# ***************************
def build_table( cnn ):

    cursor = cnn.cursor(dictionary=True)

    sql = f"""select
        社員コード,
        氏名,
        フリガナ,
        所属,
        性別,
        作成日,
        更新日,
        給与,
        手当,
        管理者,
        DATE_FORMAT(生年月日,'%Y/%m/%d') as 生年月日
        from 社員マスタ
        where 氏名 like '%{forms("条件")}%'"""

    # デバッグ
    log(sql)

    cursor.execute(sql)

    lines  = ""
    for row in cursor:

        if lines == "":
            # タイトル
            for col in row.keys():
                lines += f"<th>{col}</th>"

        cells  = ""
        for col in row.values():
            if col is None:
                cells += f"<td></td>"
            else:
                cells += f"<td>{col}</td>"
    
        lines += f"<tr>{cells}</tr>"
    
    cursor.close()

    set("lines",lines)


