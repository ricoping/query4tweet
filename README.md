# query4tweet
You can search in twitter without twitter API and get result as python object.

## How to use
<p>
You put a query or hash tag into *Query4Tsuiit* instance and set mode that decides whether you get HTML source from search result page as dynamic web page or static web page.(The mode is usually set to be *dynamic*)
</p>
<p>
You can get *timelines* of people who tweet about the query you put into by *timelines*.
</p>
<p>
You can also get *screen names* of them by *timeline_IDs*.
</p>

## Example
~~~
import query4tsuiit
twi_query = query4tsuiit.Query4Tsuiit("#花火", "dynamic")

print(twi_query.timelines) #1
print(twi_query.timeline_IDs) #2
~~~

## \#1
~~~
 {'text_body': '遣都湖に沈んだ者たちに告ぐ。今すぐNetflixに入り林遣都の「火花」全10話をみるんだ。一ヶ月無料だから見上げられる。私は本日1日で全部見た。「生きる」という物哀しくも美しい営みを静謐に描く傑作。\n'
               '\n'
               '林遣都の徳永むちゃくちゃいいよ！！！\n'
               '\n'
               '#おっさんずラブ\n'
               '#林遣都の大飢饉\n'
               '#花火\n'
               '#林遣都',
  'tl_fav_div': 1,
  'tl_rt_div': 1,
  'twi_abs_url': 'https://twitter.com/_KAI_ORIGAMI__/status/1097507737431203840',
  'user_id': '_KAI_ORIGAMI__',
  'user_name': 'KAI'},
 {'text_body': 'へっ！汚ねえ花火だ！\n'
               '\n'
               '13万ポイント！\n'
               'とりあえず4分の1行ったぜ！\n'
               'ありがとうございますだ！\n'
               '\n'
               '#SHOWROOM\n'
               '#花火 pic.twitter.com/4mdl1wYB3v',
  'tl_fav_div': 3,
  'tl_rt_div': 0,
  'twi_abs_url': 'https://twitter.com/tugasin/status/1097809411886571520',
  'user_id': 'tugasin',
  'user_name': 'ニラータ@睡眠中'},
 {'text_body': '河口湖冬花火、今年２回目の撮影。満月２日前で月明かりを期待しましたが\n'
               '霞が酷くて富士山がハッキリしません\n'
               '１枚目\u3000\u3000\u3000河口湖大橋から逆さが確認出来た時間帯と合成\n'
               '２枚目\u3000\u3000\u3000花火後撮りとの合成\n'
               '３・４枚目\u3000合成無し１枚撮り\n'
               '\n'
               '#富士山\n'
               '#花火\n'
               '#河口湖pic.twitter.com/DpBGibpPvp',
  'tl_fav_div': 40,
  'tl_rt_div': 1,
  'twi_abs_url': 'https://twitter.com/m4152saka/status/1097492898596057088',
  'user_id': 'm4152saka',
  'user_name': 'クリスタル'},
 {'text_body': '2019/02/17\n'
               "GPVの予報通り、夜になると雲がなくなって富士山が見えてきましたっ٩( 'ω' )و \n"
               '#花火\n'
               '#河口湖冬花火\n'
               '#富士山\n'
               '#fujidelicpic.twitter.com/Pl3EQSRRTV',
  'tl_fav_div': 82,
  'tl_rt_div': 6,
  'twi_abs_url': 'https://twitter.com/mikatophoto/status/1097488563740893184',
  'user_id': 'mikatophoto',
  'user_name': 'ミカ'}]

~~~

## \#2
~~~
[
 'amn0617',
 '_KAI_ORIGAMI__',
 'AnneNakamura',
 'ArashianMcz',
 'htana27',
 'fujibi3776'
 ]
~~~
