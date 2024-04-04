from gruut import sentences
from collections.abc import Iterable

from openphonemizer import OpenPhonemizer
phonemizer = OpenPhonemizer()

class PhonemeConverter:
    def phonemize(self, text):
        pass


class GruutPhonemizer(PhonemeConverter):
    def phonemize(self, text, lang='en-us'):
        return phonemizer(text)


# class YourPhonemizer(Phonemizer):
#     def phonemize(self, text):
#         ...


class PhonemeConverterFactory:
    @staticmethod
    def load_phoneme_converter(name: str, **kwargs):
        if name == 'gruut':
            return GruutPhonemizer()
        else:
            raise ValueError("Invalid phoneme converter.")
