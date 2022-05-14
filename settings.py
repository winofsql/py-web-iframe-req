import cgi
import sys
import io
import pprint

# **************************************
# デバッグログの初期化
# **************************************
with open('debug.log', 'w', encoding='utf-8') as f:
    print("開始",end='\n',file=f)

# **************************************
# グローバル変数
# **************************************
pp = None

# **************************************
# 共有ディクショナリ
# **************************************
val = {}
val["pass"] = "1"
val["check_message"] = ""
val["lines"] = ""

# **************************************
# フォーム用変数
# **************************************
fld_names = {}
form = {}
form_data = {}

# **************************************
# CGI 初期処理
# **************************************
def cgi_init():

    global pp
    global form

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    print("Content-Type: text/html; charset=utf-8")
    print( "Expires: Thu, 19 Nov 1981 08:52:00 GMT" )
    print( "Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0" )
    print( "Pragma: no-cache" )
    print()

    pp = pprint.PrettyPrinter(indent=4)

    form = cgi.FieldStorage()

# **************************************
# データの整形表示
# **************************************
def print_r(data):

    global pp

    print("<pre>")
    pp.pprint(data)
    print("</pre>")

# **************************************
# フォームデータの取得
# **************************************
def forms(target, set_data=None):

    global fld_names
    global form

    if set_data is not None:
        form_data[fld_names[target]] = set_data
        return

    result = ""

    if form_data.get(fld_names[target]) is not None:
        return( form_data[fld_names[target]] )

    if not fld_names[target] not in form:
        result = form[fld_names[target]].value

    return(result)

# **************************************
# フォームフィールド名取得
# **************************************
def fields(target):

    return(fld_names[target])

# **************************************
# フォームフィールドセット設定
# **************************************
def set_field_names( field_set ):

    global fld_names

    fld_names = field_set

# **************************************
# ディクショナリ : set & get
# **************************************
def set( my_key, my_val ):

    global val
    val[my_key] = my_val

def get( my_key ):

    global val
    return( val[my_key] )

# **************************************
# ログ出力
# **************************************
def log( message ):
    with open('debug.log', 'a', encoding='utf-8') as f:
        print(message,end='\n',file=f)
    
# **************************************
# ログ出力( pprint )
# **************************************
def pplog( obj ):

    with open("debug.log", "a", encoding='utf-8') as f:
        pprint.pprint(obj, stream=f)


