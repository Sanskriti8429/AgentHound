class SharedMemory:
    def __init__(self):
        self.entries= []

    def write(self, author: str, content: str):
        self.entries.append({"author": author, "content": content})

    def read_all(self)-> str:
        return "\n".join(f"- ({e['author']}): {e['content']}" for e in self.entries)

if __name__=="__main__":
    memory= SharedMemory()
    memory.write("research_agent", "some fake finding")
    print(memory.read_all())