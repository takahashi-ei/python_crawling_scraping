
# coding: utf-8

# # grepとcutコマンドを使う

# 下記のようにcutコマンドを使うと、条件を満たす場所を取り出すことができる<br>
# sed -e 's/.*(探索する単語).*/\1/'<br>
# 例えば下のようになる

# $ echo 'abcdefghijklmn' | sed -e "s/.*\(d.).*/\1\"<br>
# de

# 下記のようにすると、条件を満たす場所を取り除くことができる<br>
# sed -e 's/(取り除きたい場所にマッチする正規表現)//g'<br>
# これを使うことで、sample.htmlからページの情報を取り出すことができる

# $cat sample_page.html | grep -E 'class="paging-number".*-' | sed -E 's/,[^>]*>//g'<br>
# 1 - 30 / 2162

# In[ ]:



