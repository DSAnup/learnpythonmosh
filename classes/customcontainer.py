class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    # count the number of item
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    # set value
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
print(cloud["python"])
cloud["python"] = 10
cloud.add("Python")
cloud.add("Python")
cloud.add("Python")
cloud.add("Java")
print(cloud.tags)
print(cloud.__len__())
print(cloud.__dict__)
