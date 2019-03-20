# misc-Bubble Babble

## origin: a ctf from 17guangdongQW
https://blog.csdn.net/qq_40980391/article/details/79828125

Get a file called flag.enc, which contents: xinik-samak-luvag-hutaf-fysil-notok-mepek-vanyh-zipef-hilok-detok-damif-cusol-fezyx





## encoding way
In computing, Bubble Babble is a binary data encoding designed by Antti Huima. This encoding uses alternation of consonants and vowels to encode binary data to pseudowords that can be pronounced more easily than arbitrary lists of hexadecimal digits. While Bubble Babble is technically a binary encoding, it also acts as a 65,536-digit positional number system with a one-to-one mapping from each five-character sequence to 16 bits of data.


source:
http://wiki.yak.net/589
http://bohwaz.net/archives/web/Bubble_Babble.html



php script:
http://bohwaz.net/p/Bubble-Babble-CLI-encoder-decoder






python script:
https://github.com/eur0pa/bubblepy

Usage:

  from BubblePy import BubbleBabble
  bb = BubbleBabble()
  print bb.encode('Pineapple')
  print bb.decode('xigak-nyryk-humil-bosek-sonax')