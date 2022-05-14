import os
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

<div id="head">
    <p class="ttl">
        氏名で検索
    </p>
    <p class="entry">
        <input
            id="cond"
            type="text">
        <input
            class="ml-4 btn btn-success"
            id="btn"
            type="button"
            value="問合せ">

        <a
            class="ml-4 btn btn-info btn-sm"
            href="{os.path.basename(get("base_name"))}">GET 再読み込み</a>	
    </p>
    <p class="line"></p>

    <h4 class="text-danger">{get("check_message")}</h4>

</div>

<iframe id="extend" name="extend" class="iframe-option" src="req/control.py"></iframe>

</body>
</html>"""


print(out_client)
