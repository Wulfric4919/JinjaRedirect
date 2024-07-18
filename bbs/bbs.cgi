#!/usr/bin/perl

require "jcode.pl";

# 漢字コード
# （EUCにする場合は、$charset="euc-jp" と $kcode="euc" を設定）
$charset = "Shift_JIS";
$kcode = "sjis";

# 現在の時刻($time)を求めておく
($sec, $min, $hour, $mday, $mon, $year) = localtime();
$time = sprintf("%04d/%02d/%02d %02d:%02d:%02d",
    $year + 1900, $mon + 1, $mday, $hour, $min, $sec);

# フォームデータを読み込む
read(STDIN, $buf, $ENV{'CONTENT_LENGTH'});
foreach (split(/&/, $buf)) {
    ($name, $value) = split(/=/);
    $value =~ tr/+/ /;
    $value =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack("C", hex($1))/eg;
    $value =~ s/&/&amp;/g;
    $value =~ s/</&lt;/g;
    $value =~ s/>/&gt;/g;
    $value =~ s/"/&quot;/g;
    jcode::convert(*value, $kcode);    # 漢字コードを変換しておく
    $FORM{$name} = $value;
}

# メッセージの改行を <br> に置換する
$FORM{'MESG'} =~ s/(\r\n|\n|\r)/<br>\n/g;

# ファイルに追加書き込みする
if ($FORM{'MESG'} ne "") {
    $msg = "<hr>\n"
         . "<div class=header>\n"
         . "<span class=name>$FORM{'NAME'}</span>\n"
         . "<span class=time>$time</span>\n"
         . "</div>\n"
         . "<div class=mesg>$FORM{'MESG'}</div>\n";
    open(OUT, ">> bbs.txt") || ErrorExit("書き込み失敗。");
    print OUT $msg || ErrorExit("書き込み失敗。");
    close(OUT) || ErrorExit("書き込み失敗。");
}
