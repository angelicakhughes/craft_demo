def greeter(prefix):
    other_name = prefix + "lala"

    def greet(name):
        print(f"{prefix} {name}")
    return greet

hello = greeter("Hello,")
goodbye = greeter("Goodbye")

hello("Kevin")
goodbye("Kyle")
