
class Stack:

    def __init__(self, staples=""):
        self.staples = staples

    def isEmpty(self):
        if len(self.staples) == 0:
            return True
        else:
            return False

    def push(self, new_element):
        self.staples += new_element

    def pop(self):
        last_element = self.staples[-1]
        self.staples = self.staples[:-1]
        return last_element

    def peek(self):
        return self.staples[-1]

    def size(self):
        return len(self.staples)

    def check_balance(self):
        if self.isEmpty() == False:
            if len(self.staples) % 2 == 0:
                if self.staples[0] not in ")]}" or self.staples[-1] in "([{":
                    check_list = []
                    for staple in self.staples:
                        if staple in "([{":
                            check_list.append(staple)
                        elif staple in ")]}":
                            if check_list[-1] == "(" and staple == ")":
                                check_list.pop()
                            elif check_list[-1] == "[" and staple == "]":
                                check_list.pop()
                            elif check_list[-1] == "{" and staple == "}":
                                check_list.pop()
                            else:
                                return "Несбалансированно"
                    if len(check_list) == 0:
                        return "Сбалансированно"
                    else:
                        return "Несбалансированно"
                else:
                    return "Несбалансированно"
            else:
                return "Несбалансированно"
        else:
            return "Последовательность пуста"


if __name__ == "__main__":

    ex_1 = "(((([{}]))))"
    ex_2 = "[([])((([[[]]])))]{()}"
    ex_3 = "{{[()]}}"
    ex_4 = "}{}"
    ex_5 = "{{[(])]}}"
    ex_6 = "[[{())}]"

    ex_7 = "[{]}"
    ex_8 = "([[](({}))])(["
    ex_9 = "(()[[]]){[()][]}[(())]"
    ex_10 = "[]()(){}(())[]"
    ex_11 = "[[[(({(())"

    ex_12 = "{}"
    ex_13 = ""

    examples = [ex_1, ex_2, ex_3, ex_4, ex_5, ex_6, ex_7, ex_8, ex_9, ex_10, ex_11, ex_12, ex_13]

    # Прогоним все примеры последовательностей через метод проверки сбалансированности:
    for example in examples:
        stack = Stack(example)
        print(f"{example} >>> {stack.check_balance()}")

    print("\n------------------\n")

    # Создадим новую пустую последовательность и провеим методы:
    new_stack = Stack()
    print(f"isEmpty(): {new_stack.isEmpty()}")
    new_stack.push("Hv93Ds;{}R")
    print(f"stack after push(): {new_stack.staples}")
    print(f"pop(): {new_stack.pop()}")
    print(f"peek(): {new_stack.peek()}")
    print(f"current stack: {new_stack.staples}")
    print(f"size(): {new_stack.size()}")
    print(f"isEmpty(): {new_stack.isEmpty()}")