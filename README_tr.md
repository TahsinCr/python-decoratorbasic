<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

[<img src="images/languages/turkish-flag.png" height="28" alt="Logo" >][lang-tr-url]
[<img src="images/languages/british-flag.png" height="28" alt="Logo" >][lang-en-url]

<br />






<!-- About -->
<div align="center">

[<img src="images/logo.png" alt="Logo">][project-url]

<h3 align="center">Python DecoratorBasic</h3>

<p align="center">

Python'da decorator oluşturmak ve yönetmek için basit araçlar.

[Changelog][changelog-url] · [Report Bug][issues-url] · [Request Feature][issues-url]
 
</p>

</div>






<!-- TABLE OF CONTENTS -->

<details>

<summary>İçindekiler</summary>

<ol>

<li>

<a href="#about-the-project">Proje hakkında</a>

<ul>

<li><a href="#built-with">İle İnşa Edildi</a></li>

</ul>

</li>

<li>

<a href="#getting-started">Başlarken</a>

<ul>

<li><a href="#prerequisites">Önkoşullar</a></li>

<li><a href="#installation">Kurulum</a></li>

</ul>

</li>

<li><a href="#usage">Kullanım</a></li>

<li><a href="#roadmap">Yol haritası</a></li>

<li><a href="#contributing">Katkı</a></li>

<li><a href="#license">Lisans</a></li>

<li><a href="#contact">İletişim</a></li>

<li><a href="#acknowledgments">Teşekkürler</a></li>

</ol>

</details>






<!-- ABOUT THE PROJECT -->

##  Proje hakkında

Python 3.x'e basit decorator araçları sağlar.

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>

###  İle İnşa Edildi

* [![python-shield][python-shield]][pypi-project-url]

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






<!-- GETTING STARTED -->

##  Başlarken

Yerel bir kopyayı çalışır duruma getirmek için bu basit örnek adımları izleyin.

###  Önkoşullar

* Python-lib - [CallableType][pythonlib-callabletype], gelişmiş tip kontrolü için kullanılmıştır.

###  Kurulum

1. Depoyu klonla
```sh
git clone https://github.com/TahsinCr/python-decoratorbasic.git
```

2. PIP paketlerini kurun
```sh
pip install decoratorbasic
```

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






<!-- USAGE EXAMPLES -->

##  Kullanım

Timer adında bir decorator oluşturalım.
```python
from typing import Any, Callable, TypeVar, Generic
import time

from decoratorbasic import (
    DecoratorBasic, get_decorator_callable, get_decorators
)
TCallable = TypeVar('TCallable', bound=Callable)    

class TimerDecorator(DecoratorBasic[TCallable], Generic[TCallable]):
    def definator(self, callable:TCallable):
        print(f"Add Decorator '{callable.__name__}': '{self.__class__.__name__}'")
        return callable

    def decorator(self, callable:TCallable, *args, **kwargs):
        self.start = time.time()
        result = callable(*args, **kwargs)
        self.end = time.time()
        print(f"Result '{callable.__name__}': {self.end - self.start}")
        return result

@TimerDecorator()
def test_range(start:int, stop:int):
    for n in range(start, stop): ...

@TimerDecorator()
class testo:
    def __init__(self):
        for n in range(1, 10000000):...

test_range(1,4000000)

print('DecoratorFunction: {}; BaseFuntion: {}'.format(test_range, get_decorator_callable(test_range)))

print('Decorators: {}'.format(str(get_decorators(test_range))))

testo()

```
Çıktı
```
Add Decorator 'test_range': 'TimerDecorator'
Add Decorator 'testo': 'TimerDecorator'
Result 'test_range': 0.06389307975769043
DecoratorFunction: <function test_range at 0x000001C8395540E0>; BaseFuntion: <function test_range at 0x000001C839161440>
Decorators: [<__main__.TimerDecorator object at 0x000001C8393C1400>]
Result '__init__': 0.1724531650543213
```

<br>

_Daha fazla örnek için lütfen [belgelere][wiki-url] bakın_

Önerilen özelliklerin (ve bilinen sorunların) tam listesi için [açık sorunlara][issues-url] bakın.

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






<!-- ROADMAP -->

##  Yol haritası

- [ ] Dökümantasyon ekle.

Önerilen özelliklerin (ve bilinen sorunların) tam listesi için [açık sorunlara][issues-url] bakın.

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






<!-- CONTRIBUTING -->

##  Katıkı

Katkılar, açık kaynak topluluğunu öğrenmek, ilham vermek ve yaratmak için harika bir yer yapan şeydir. Yaptığınız tüm katkılar **çok makbule geçer**.

Bunu daha iyi hale getirecek bir öneriniz varsa, lütfen repoyu çatallayın ve bir çekme isteği oluşturun. Ayrıca "geliştirme" etiketiyle bir sorun açabilirsiniz.

Projeye yıldız vermeyi unutmayın! Tekrar teşekkürler!

1. Projeyi çatallayın

2. Özellik Dalınızı oluşturun (`git checkout -b feature/AmazingFeature`)

3. Değişikliklerinizi taahhüt edin (`git commit -m 'Add some AmazingFeature'`)

4. Şubeye Gönderin (`git push origin feature/AmazingFeature`)

5. Bir Çekme İsteği Açın

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






<!-- LICENSE -->

##  Lisans

MIT Lisansı altında dağıtılmaktadır. Daha fazla bilgi için [LICENSE][license-url] konusuna bakın.

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






<!-- CONTACT -->

##  İletişim

Email: TahsinCr@outlook.com

X: [@TahsinCrs][x-url]

LinkedIn: [TahsinCr][linkedin-url]

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






<!-- ACKNOWLEDGMENTS -->

##  Teşekkürler

* [PyPI][pypi-project-url]

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






<!-- IMAGES URL -->

[python-shield]: https://img.shields.io/pypi/pyversions/decoratorbasic?style=flat-square

[contributors-shield]: https://img.shields.io/github/contributors/TahsinCr/python-decoratorbasic.svg?style=for-the-badge

[forks-shield]: https://img.shields.io/github/forks/TahsinCr/python-decoratorbasic.svg?style=for-the-badge

[stars-shield]: https://img.shields.io/github/stars/TahsinCr/python-decoratorbasic.svg?style=for-the-badge

[issues-shield]: https://img.shields.io/github/issues/TahsinCr/python-decoratorbasic.svg?style=for-the-badge

[license-shield]: https://img.shields.io/github/license/TahsinCr/python-decoratorbasic.svg?style=for-the-badge

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555



<!-- Github Project URL -->

[project-url]: https://github.com/TahsinCr/python-decoratorbasic

[pypi-project-url]: https://pypi.org/project/decoratorbasic

[contributors-url]: https://github.com/TahsinCr/python-decoratorbasic/graphs/contributors

[stars-url]: https://github.com/TahsinCr/python-decoratorbasic/stargazers

[forks-url]: https://github.com/TahsinCr/python-decoratorbasic/network/members

[issues-url]: https://github.com/TahsinCr/python-decoratorbasic/issues

[wiki-url]: https://github.com/TahsinCr/python-decoratorbasic/wiki

[license-url]: https://github.com/TahsinCr/python-decoratorbasic/blob/master/LICENSE

[changelog-url]:https://github.com/TahsinCr/python-decoratorbasic/blob/master/CHANGELOG.md



<!-- Contacts URL -->

[linkedin-url]: https://linkedin.com/in/TahsinCr

[x-url]: https://twitter.com/TahsinCrs



<!-- File URL -->

[lang-tr-url]: https://github.com/TahsinCr/python-decoratorbasic/blob/master/README_tr.md

[lang-en-url]: https://github.com/TahsinCr/python-decoratorbasic/blob/master/README.md

<!-- Dependencies URL -->

[pythonlib-callabletype]: https://github.com/TahsinCr/python-callabletype
