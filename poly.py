#polymorphism - one taking many form
#duck-typing
class Filemanager:
    def store(self):
        print("image,video")
class Word:
    def store(self):
        print("word.doc")


class Pc:
    def func(self,apps):
        apps.store()

# apps = Filemanager()
apps = Word()

pc1 = Pc()
pc1.func(apps)


