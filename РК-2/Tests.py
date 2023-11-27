import unittest
from main import *


class TestRK2(unittest.TestCase):
    # Компьютеры
    files = [
        File(1, 'Laba_1', 2.4, 1),
        File(2, 'Laba_2', 2.1, 1),
        File(3, 'Laba_3', 1.8, 1),
        File(4, 'Курсовая', 3.5, 2),
        File(5, 'Макет', 4.0, 2),
        File(6, 'ДЗ_Физика', 1.4, 3)
    ]

    # Микропроцессоры
    catalog_files = [
        Catalog_Files(1, 'Лабораторные', 5.0),
        Catalog_Files(2, 'ИУ-5', 7.5),
        Catalog_Files(3, 'Семестр_3', 1.4)
    ]

    def test_A1(self):
        one_to_many = [(f.name, f.size, c.name)
                       for f in Files
                       for c in Catalogs_Files
                       if f.id_Cat == c.id]
        self.assertEqual(Solution1(one_to_many),
                         [('Laba_1', 2.4, 'Лабораторные'),
                          ('Laba_2', 2.1, 'Лабораторные'),
                          ('Laba_3', 1.8, 'Лабораторные'),
                          ('ДЗ_Физика', 1.4, 'Семестр_3'),
                          ('Курсовая', 3.5, 'ИУ-5'),
                          ('Макет', 4.0, 'ИУ-5')])

    def test_A2(self):
        one_to_many = [(f.name, f.size, c.name)
                       for f in Files
                       for c in Catalogs_Files
                       if f.id_Cat == c.id]
        self.assertEqual(Solution2(one_to_many),
                         [('ИУ-5', 7.5), ('Лабораторные', 6.3), ('Семестр_3', 1.4)])

    def test_A3(self):
        many_to_many_temp = [(c.name, FC.id_Fi, FC.id_Cat)
                             for c in Catalogs_Files
                             for FC in Fi_Cats
                             if c.id == FC.id_Cat]

        many_to_many = [(Cat_name, f.name, f.size,)
                        for Cat_name, FC_id_Fi, FC_id_Cat in many_to_many_temp
                        for f in Files if f.id == FC_id_Fi]
        self.assertEqual(Solution3(many_to_many),
                         {'Лабораторные': ['Laba_1', 'Laba_2', 'Laba_3']})


if __name__ == '__main__':
    unittest.main()