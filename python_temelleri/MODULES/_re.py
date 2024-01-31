import re

result = dir(re)

# re module


str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

#re.findall()

# result = re.findall("Python",str)
# result = len(result)

# re.split()

# result = re.split(" ",str)
# result = re.split("r",str)

#re.sub()

# result = re.sub(" ","-",str)
# result = re.sub("\s","-",str) # \s boşluk karakterini ifade eder yukarıdaki işlemle aynı görevi görmüş olur.

# re.search()

# result = re.search("Python",str) 
# result = result.span() #Yukarıda Python kelimesini aramıştık burada ise Python kelimesinin sadedce hangi indexlerde olduğunu bize verir.
# result = result.start() #Hangi karakterden başladığını bize söyler.
# result = result.end() # Bitiş karakterinin indisi
# result = result.group()
# result = result.string



# regular expression

"""

    []-Köşeli parantezler arasına yazılan bütün karakterler
        aranır.

        [abc] => a      : 1 match
                 ac     : 2 match
                 Python : No matches

        [a-e]   =>  [abcde]
        [1-5]   =>[12345]
        [0-39]  =>[01239]

        [^abc]  =>  abc dışındaki karakterler.
        [^0-9]  =>  Rakam olmayan karakterler.

"""

result = re.findall("[abc]", str)
result = re.findall("[sat]", str)
result = re.findall("[a-e]", str)
result = re.findall("[a-z]", str)
result = re.findall("[1-5]", str)
result = re.findall("[^abc]", str)
result = re.findall("[^0-9]", str)


"""
        . - Herhangi bir tek karakteri belirtir.
            ..  =>  a   : No match
                    ab  : 1 match
                    abc : 1 match
                    abcd: 2 matches

"""

result = re.findall("...",str)
result = re.findall("Py..on",str)


"""

    ^ - Belirtilen karakterlerle başlıyor mu?

    ^a  =>  a:      1 match
            abc:    1 match
            bac:    No match

"""

result = re.findall("^P",str)

"""

    $ - Belirtilen karakterlerle başlıyor mu?

    a$  =>  a       : 1 match
            lamba   : 1 match
            Python  : No match

"""

result = re.findall("t$",str)
result = re.findall("saat$",str)
result = re.findall("saatt$",str)


"""

    * - Bir karakterin sıfır ya da daha fazla sayıda olmasını
        kontrol eder.

        ma*n => mn      : 1 match
                man     : 1 match
                maaan   : 1 match
                main    : No match (a' nın arkasına n gelmiyor.)

"""

result = re.findall("sa*t",str)

"""

    + - Bir karakterin sıfır ya da daha fazla sayıda olmasını
        kontrol eder.

        ma+n => mn      : 1 match
                man     : 1 match
                maaan   : 1 match
                main    : No match (a' nın arkasına n gelmiyor.)

"""

result = re.findall("sa+t",str)

"""

    ? - Bir karakterin sıfır ya da bir kez olmasını
        kontrol eder.

        ma?n => mn      : 1 match
                man     : 1 match
                maaan   : 1 match
                main    : No match (a' nın arkasına n gelmiyor.)

"""

result = re.findall("sa?t",str)

"""

    {} - Karakter sayısını kontrol eder.

        al{2}   => a karakterinin arkasına 1 karakteri 2 kez tekrarlamalı.
        al{2,3} => a karakterinin arkasına 1 karakteri en az 2 en fazla 3 kez tekrarlamalı.
        [0-9]{2,4}  => en az 2 en çok 4 basamaklı sayılar.
"""

result = re.findall("a{2}",str)
result = re.findall("[0-9]{2}",str)

"""
    | - alternatif seçeneklerden birinin gerçekleşmesi gerekir.
        a|b => a ya da b

            cde =>  no match
            ade =>  1 match
            acdbea => 3 match

"""

"""
    () - gruplamak için kullanılır.

        (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir.
"""

"""
    \ - Özel karakterleri aramamızı sağlar.
        \$ => $ karakterinin arkasına a karakterini arar. Yani
              $ regula exp. engine tarafından yorumlanmaz.

    \A - Belirtilen karakter stringin başında mı?
        \Athe => the string in başında mı?

    \Z - Belirtilen karakter stringin başında mı?
        the\Z => the string in sonunda mı?

    \b - Belirtilen karakter kelimenin başında ya da sonunda mı?
        \bthe => the string in başında mı?
        the\b => the string in sonunda mı?

    \B - Belirtilen karakter kelimenin başında ya da sonunda değil mi?
        \Bthe => the string in başında değil mi?
        the\B => the string in sonunda değil mi?

    \d - [0-9] ile aynı anlama gelir yani rakamları ara.
        \d => 12abc34

    \D - [^0-9] ile aynı anlama gelir yani rakamları ara.
        \D => 12ab44_50

    \s - Boşluk karakterlerini arar. 
    \S - Boşluk karakteri dışındakiler
    \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri.
    \W - \w nin tam tersi
"""

result = re.findall("\APython",str)
result = re.findall("saat\Z",str)

print(result)

