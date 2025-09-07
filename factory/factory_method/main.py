from .store import NYPizzaStore, ChicagoPizzaStore

def main():
    ny = NYPizzaStore(); chi = ChicagoPizzaStore()
    print("=== Nueva York ===")
    p1 = ny.order_pizza("cheese");    print("Ethan ordered:", p1)
    p2 = ny.order_pizza("veggie");    print("Alice ordered:", p2)
    p3 = ny.order_pizza("pepperoni"); print("Karen ordered:", p3)
    print("=== Chicago ===")
    p4 = chi.order_pizza("cheese");    print("Joel ordered:", p4)
    p5 = chi.order_pizza("veggie");    print("Bob ordered:", p5)
    p6 = chi.order_pizza("pepperoni"); print("Lucas ordered:", p6)

    

if __name__ == "__main__":
    main()