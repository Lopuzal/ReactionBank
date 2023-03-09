import imgbank
import os


bank = imgbank.Imgbank(True)

class TestImgbank:

    def __init__(self):
        self.bank = imgbank.Imgbank("test.db")
        self.bank.init_db()

    def test_add_entry(self):
        self.bank.add_entry("image1", ["golri","test","humour"])
        self.bank.add_entry("image2", ["golri","blague","humour"])
        self.bank.add_entry("image3", ["triste","mec","solitaire","pas drôle"])
        self.bank.add_entry("image4", ["humour","aeoaeoaoeaoe"])
        self.bank.add_entry("image5", ["humour","greentext","564ze9r87ze6r54","arena","videogame"])

    def test_delete_entry(self):
        self.bank.delete_entry(4)

    def test_tags_list_to_image_paths_list(self):
        list1 = self.bank.tags_list_to_image_paths_list(["golri"])
        print(list1)
        assert(list1 == ["image1","image2"])

        list2 = self.bank.tags_list_to_image_paths_list(["triste"])
        print(list2)
        assert(list2 == ["image3"])


        list3 = self.bank.tags_list_to_image_paths_list(["humour"])
        print(list3)
        assert(list3 == ["image1","image2","image5"])

    def test_all(self):
        self.test_add_entry()
        self.test_delete_entry()
        self.test_tags_list_to_image_paths_list()


if __name__ == "__main__":
    tests = TestImgbank()
    tests.test_all()