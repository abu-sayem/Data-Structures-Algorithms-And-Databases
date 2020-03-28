class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        store = []
        for i in range(1, n+1):
            str = ""
            if i % 3 == 0:
                str = str + "Fizz"
            if i % 5 == 0:
                str = str + "Buzz"
            if str == "":
                str = str + f"{i}"
            store.append(str)
        return store
