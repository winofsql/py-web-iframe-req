# **************************************
# 親ディレクトリに参照パス追加
# **************************************
import sys
sys.path.append('..')

#import os
# **************************************
# 共有メソッド
# **************************************
from settings import *
# **************************************
# js 選択
# **************************************
js = "entry.js";
#js = "entry-json.js";

# **************************************
# js キャッシュ用
# **************************************
from datetime import datetime
tm = datetime.now().strftime("%Y%m%d%H%M%S")

# **************************************
# 画面定義
# **************************************
out_client = f"""<!DOCTYPE html>
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.1/css/bootstrap.css" />

<script src="{js}?{tm}"></script>

<link rel="stylesheet" href="entry.css?{tm}">
</head>
<body>

    <table class="table table-hover">
        <tbody id="tbl">
            {get("lines")}
        </tbody>
    </table>

</body>
</html>"""


print(out_client)

pplog(fld_names)
pplog(val)
pplog(form)